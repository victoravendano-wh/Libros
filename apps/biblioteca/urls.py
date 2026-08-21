from django.conf.urls import url, include
from django.contrib import admin


# from .views import hola, fecha_actual
from .views import  resultado, contactos



urlpatterns = [
    url(r"^contacto/$", contactos, name=""),
    url(r'^buscar/$', resultado, name='resultado'),
]
