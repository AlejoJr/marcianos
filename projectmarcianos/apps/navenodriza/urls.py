from django.conf.urls import url
from django.urls import path, re_path
from apps.navenodriza.views import navenodriza_lista, navenodriza_view, navenodriza_edit, navenodriza_delete

app_name = "navenodriza"
urlpatterns = [
    #url(r'^inicio$', index, name='index'),
    url(r'^$', navenodriza_lista, name='navenodriza_lista'),
    url(r'^nuevo$', navenodriza_view, name='navenodriza_crear'),
    url(r'^editar/(?P<id_navenodriza>\d+)/$', navenodriza_edit, name='navenodriza_editar'),
    url(r'^eliminar/(?P<id_navenodriza>\d+)/$', navenodriza_delete, name='navenodriza_eliminar'),
]