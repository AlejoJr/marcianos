"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView

urlpatterns = [
    #re_path(r'^index/', include('apps.navenodriza.urls')),
    #path('admin/', admin.site.urls),
    #re_path(r'^navenodriza/', include('apps.navenodriza.urls')),
    #re_path(r'^aeronave/', include('apps.aeronave.urls')),
    #re_path(r'^pasajero/', include('apps.pasajero.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^navenodriza/', include('apps.navenodriza.urls', namespace='navenodriza')),
    url(r'^aeronave/', include('apps.aeronave.urls', namespace='aeronave')),
    url(r'^pasajero/', include('apps.pasajero.urls', namespace='pasajero')),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    url(r'^$', LoginView.as_view(template_name='index.html'),name="login"),

]
