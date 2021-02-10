llamadas_cluster$COD_LOCALIDAD = NULL
llamadas_cluster$POBLACION = NULL
llamadas_cluster$RATIO = NULL
llamadas_cluster$CANT_LLAMADAS = NULL


#eliminamos las ciudades donde no se han registrado llamadas
llamadas_cluster = llamadas_cluster[-c(20), ]


#eliminamos valores
llamadas_cluster$nombre= NULL
llamadas_cluster$cluster= NULL

#redondeamos los valores a dos decimales
llamadas_cluster[,-1] <-round(llamadas_cluster[,-1],2)
