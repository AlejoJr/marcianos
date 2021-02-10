#colocamos una semilla
set.seed(123)
#ahora bien dividiremos la data y agruparemos en 6 grupos
km.res <- kmeans(llamadas_cluster, 6, nstart = 50)


#cluster obtenido
print(km.res)
head(km.res$cluster, 4)

#Visualizando la data obtenida
fviz_cluster(km.res, data = llamadas_cluster)
