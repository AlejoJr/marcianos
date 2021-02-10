km.res <- kmeans(llamadas_cluster, 5, nstart = 50)

#cluster obtenido
print(km.res)
head(km.res$cluster, 4)

#tamaño
km.res$size

#medianas 
km.res$centers

#Visualizando la data obtenida
fviz_cluster(km.res, data = llamadas_cluster)
