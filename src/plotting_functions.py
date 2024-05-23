def draw_interp_plots(series,        # Serie de pandas con datos de tiempo
                      country,       # Lista de códigos de países para graficar
                      ylabel,        # Etiqueta para el eje y
                      xlabel,        # Etiqueta para el eje x
                      color_mapping, # Diccionario mapeando códigos de país a colores
                      code_to_name,  # Diccionario mapeando códigos de país a nombres completos
                      lw,            # Ancho de línea para los gráficos
                      logscale,      # Booleano para aplicar escala logarítmica al eje y
                      ax             # Eje de matplotlib donde dibujar los gráficos
                     ):

    for c in country:
        # Obtiene los datos interpolados solo en áreas internas, excluyendo los extremos
        df_interpolated = series[c].interpolate(limit_area='inside')
        # Extrae solo los datos que han sido interpolados
        interpolated_data = df_interpolated[series[c].isnull()]

        # Dibuja los datos interpolados con líneas discontinuas
        ax.plot(interpolated_data,
                linestyle='--',
                lw=lw,
                alpha=0.7,  # Transparencia de la línea
                color=color_mapping[c])

        # Dibuja los datos originales con líneas sólidas
        ax.plot(series[c],
                lw=lw,
                color=color_mapping[c],
                alpha=0.8,  # Transparencia de la línea
                label=code_to_name.loc[c]['country'])
        
        # Aplica escala logarítmica si 'logscale' es True
        if logscale:
            ax.set_yscale('log')
    
    # Dibuja la leyenda fuera del gráfico para evitar solapamiento con las líneas
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=False)
    # Configura las etiquetas de los ejes
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    # Establece un límite de visibilidad para evitar que la leyenda oculte los datos
    ax.set_xlim(series.index.min(), series.index.max())
