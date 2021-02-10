km.res <- kmeans(llamadas_cluster, 5, nstart = 50)

#cluster obtenido
print(km.res)
head(km.res$cluster, 4)
