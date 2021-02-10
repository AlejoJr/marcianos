ggplot(delitos_mas_frecuentes_2019, aes(x = NUM_DELITOS, y=NOMBRE_DELITO, color=TIPO_INCIDENTE)) +
geom_col() + theme(legend.position = "top") +
labs(title = "Cantidad de incidentes del 2019", subtitle = "Basado en su tipo", x = "Número de delitos (en miles)", color="Codigo de incidente", y = "Incidentes" ) +
guides(colour = guide_legend(override.aes = list(size=10))) + theme(legend.key = element_rect(fill = "white"))
