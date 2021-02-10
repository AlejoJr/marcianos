for (i in 1:nrow(delitos_mas_frecuentes_2018))
{
  #filtramos tipo de accidente
  c =datos_del_2018[datos_del_2018$TIPO_INCIDENTE==delitos_mas_frecuentes_2018$TIPO_INCIDENTE[i],]
  #creamos el nombre de la columna
  colName <- paste("D_",delitos_mas_frecuentes_2018$TIPO_INCIDENTE[i], sep="")
   
  #agregamos la cantidad de llamadas anuales por localidad por cada 10000
  llamadas_localidad[colName] = c$cant_llamadas[match( llamadas_localidad$COD_LOCALIDAD, 
                                                       c$COD_LOCALIDAD)]*10000/llamadas_localidad$POBLACION
  
  llamadas_localidad[colName] <- replace( llamadas_localidad[colName],is.na( llamadas_localidad[colName]),0)
  
}
