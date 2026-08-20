from django.http import HttpResponse, Http404
import datetime


# def hola(request):
#     return HttpResponse("hola mundo")

def fecha_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body><h1>Fecha</h1><h3>%s</h3></body></html>"%ahora
    return HttpResponse(html)


def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    hora = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body><h1>Fecha</h1><h3>En %s horas serian %s</h3></body></html>"%(offset,hora)
    return HttpResponse(html)