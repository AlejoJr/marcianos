
localidad_anio_summarise <- localidad_anio_summarise %>% 
  mutate(RATIO= round(num_delitos/1000,0))

localidad_anio_summarise$NOMBRE = localities$nombre[match( localities$COD_LOCALIDAD, 
                                                           localidad_anio_summarise$COD_LOCALIDAD)]



summary(localidad_anio_summarise$RATIO)

dm<-localidad_anio_summarise[which(localidad_anio_summarise$COD_LOCALIDAD=="01"), 
                             c("ANIO","RATIO")]
plot(dm, lty=1, type="l", ylab="Delitos por distrito", xlab="aÃ±o", ylim=c(1,700), 
     col=1, xlim=c(2015,2020),
     main="Cantidad de llamadas por distrito")



for (i in 1:nrow(localities))
{
  if(i!=1){
    dm<-localidad_anio_summarise[which(
      localidad_anio_summarise$COD_LOCALIDAD==localities$COD_LOCALIDAD[i]), 
                                 c("ANIO","RATIO")]
    lines(dm,lty=2, col=i, xlim=c(2015,2020),
          main="Delitos")
  }
  
}

legend("topright", localities$nombre,
       col=c(1:nrow(localities)), lty=1:nrow(localities), cex=0.5)
