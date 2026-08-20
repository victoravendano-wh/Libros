from django.http import HttpResponse, Http404
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

# def hola(request):
#     return HttpResponse("hola mundo")

def fecha_actual(request):
    ahora = datetime.datetime.now()
    t = get_template('fecha_actual.html')
    html = t.render(Context({'fecha_actual':ahora}))
    return HttpResponse(html)

def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    hora = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body><h1>Fecha</h1><h3>En %s horas serian %s</h3></body></html>"%(offset,hora)
    return HttpResponse(html)