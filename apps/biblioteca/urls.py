from django.conf.urls import url, include
from django.contrib import admin


# from .views import hola, fecha_actual
from .views import  resultado, contactos, landing, nuevo, editar, eliminar

from .views import cbvresultado, cbvlanding#, cbvcontactos, cbvnuevo, cbveditar, cbveliminar


urlpatterns = [
    url(r"^$",landing, name="pagina-de-bienvenida"),
    url(r"^contacto/$", contactos, name="contacto"),
    url(r'^buscar/$', resultado, name='busqueda'),
    url(r"^libro/nuevo/$", nuevo, name="nuevo"),
    url(r"^libro/editar/(\d{1,2})/", editar, name="editar_libro"),
    url(r"^libro/eliminar/(\d{1,2})/", eliminar, name="eliminar_libro"),
    
    url(r"^cbv/$",cbvlanding.as_view(), name="cbv_pagina-de-bienvenida"),
    # url(r"^cbv/contacto/$", cbvcontactos.as_view(), name="cbv_contacto"),
     url(r'^cbv/buscar/$', cbvresultado.as_view(), name='cbv_busqueda'),
    # url(r"^cbv/libro/nuevo/$", cbvnuevo.as_view(), name="cbv_nuevo"),
    # url(r"^cbv/libro/editar/(\d{1,2})/", cbveditar.as_view(), name="cbv_editar_libro"),
    # url(r"^cbv/libro/eliminar/(\d{1,2})/", cbveliminar.as_view(), name="cbv_eliminar_libro"),    
    
    
    
]
