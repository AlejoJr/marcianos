
llamadas_cluster$COD_LOCALIDAD = NULL
llamadas_cluster$POBLACION = NULL
llamadas_cluster$RATIO = NULL
llamadas_cluster$CANT_LLAMADAS = NULL

#Eliminar ciudades donde no registra llamadas
llamadas_cluster = llamadas_cluster[-c(20), ]

