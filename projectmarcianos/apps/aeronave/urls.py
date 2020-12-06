from django.conf.urls import url
from django.urls import path
from apps.aeronave.views import aeronave_lista, aeronave_view, aeronave_edit, aeronave_delete

app_name = "aeronave"
urlpatterns = [
    url(r'^$', aeronave_lista, name='aeronave_lista'),
    url(r'^nuevo$', aeronave_view, name='aeronave_crear'),
    url(r'^editar/(?P<id_aeronave>\d+)/$', aeronave_edit, name='aeronave_editar'),
    url(r'^eliminar/(?P<id_aeronave>\d+)/$', aeronave_delete, name='aeronave_eliminar'),
]