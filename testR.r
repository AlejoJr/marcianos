km.res <- kmeans(llamadas_cluster, 3, nstart = 50)

km.res$size

#Visualizando la data obtenida
fviz_cluster(km.res, data = llamadas_cluster)
