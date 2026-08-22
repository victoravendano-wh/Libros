from django.conf.urls import url, include
from django.contrib import admin


# from .views import hola, fecha_actual
from .views import  resultado, contactos, landing



urlpatterns = [
    url(r"^$",landing, name="pagina-de-bienvenida"),
    url(r"^contacto/$", contactos, name="contacto"),
    url(r'^buscar/$', resultado, name='busqueda'),
]
