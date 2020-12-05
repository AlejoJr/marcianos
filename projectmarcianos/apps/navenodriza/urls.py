from django.conf.urls import url
from django.urls import path, re_path
from apps.navenodriza.views import navenodriza_lista, navenodriza_view, navenodriza_edit

app_name = "navenodriza"
urlpatterns = [
    url(r'^$', navenodriza_lista, name='navenodriza_lista'),
    url(r'^nuevo$', navenodriza_view, name='navenodriza_crear'),
    url(r'^editar/(?P<id_navenodriza>\d+)/$', navenodriza_edit, name='navenodriza_editar'),
]