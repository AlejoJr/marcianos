data_set_bogota = read.csv(file.choose(),header=TRUE, sep=';')

table(data_set_bogota$ANIO)
table(data_set_bogota$TIPO_DETALLE)
sum(data_set_bogota$CANT_INCIDENTES)

colnames(data_set_bogota)

data_set_bogota = data_set_bogota[data_set_bogota$TIPO_DETALLE != '-',]
data_set_bogota = data_set_bogota[data_set_bogota$LOCALIDAD != '-',]

data_set_bogota = data_set_bogota[data_set_bogota$COD_LOCALIDAD != '99',]
