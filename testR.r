datos_del_2018 = summarise(group_by(data_set_bogota[data_set_bogota$ANIO == 2018,],
                                        COD_LOCALIDAD,
                                        TIPO_INCIDENTE
                                    ),
                               cant_llamadas = sum(CANT_INCIDENTES))
