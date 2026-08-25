"""libros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import javascript_catalog


# from .views import hola, fecha_actual
from .views import fecha_actual, horas_adelante



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fecha/$', fecha_actual, name="hora-actual"),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante, name="fecha-adelantada"),
    url(r'^', include('apps.biblioteca.urls', namespace="app_libreria")),
    url(r'^admin/jsi18n/$', javascript_catalog, {'packages': ('django.contrib.admin',)}, name='javascript-catalog'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)