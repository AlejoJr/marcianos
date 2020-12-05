from django.conf.urls import url
from apps.pasajero.views import pasajero_lista, pasajero_view, pasajero_edit

app_name = "pasajero"
urlpatterns = [
    url(r'^$', pasajero_lista, name='pasajero_lista'),
    url(r'^nuevo$', pasajero_view, name='pasajero_crear'),
    url(r'^editar/(?P<id_pasajero>\d+)/$', pasajero_edit, name='pasajero_editar'),
]