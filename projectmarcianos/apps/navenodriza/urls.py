from django.urls import path
from . import views

urlpatterns = [
    path('', views.navenodriza_lista, name='navenodriza_lista'),
]