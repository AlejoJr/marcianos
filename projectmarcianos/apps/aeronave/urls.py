from django.conf.urls import url
from django.urls import path
from apps.aeronave.views import aeronave_lista, aeronave_view, aeronave_edit, aeronave_delete, gestionar_pasajero,gestionpasajeros_lista, aeronave_review

app_name = "aeronave"
urlpatterns = [
    url(r'^$', aeronave_lista, name='aeronave_lista'),
    url(r'^nuevo$', aeronave_view, name='aeronave_crear'),
    url(r'^editar/(?P<id_aeronave>\d+)/$', aeronave_edit, name='aeronave_editar'),
    url(r'^eliminar/(?P<id_aeronave>\d+)/$', aeronave_delete, name='aeronave_eliminar'),
    url(r'^revisar/(?P<id_aeronave>\d+)/$', aeronave_review, name='aeronave_revisar'),
    url(r'^gestionar$', gestionar_pasajero, name='gestionar_pasajero'),
    url(r'^pasajerosaeronaves$', gestionpasajeros_lista, name='pasajero_aeronaves_lista'),
]