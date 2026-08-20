from django.http import HttpResponse, Http404
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
import psycopg2

# def hola(request):
#     return HttpResponse("hola mundo")

def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {"fecha_actual":ahora})


def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    horas = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, "fecha_horas_adelante.html", {'horas':offset, 'hora_siguiente':horas})

def lista_biblioteca(request):
    db = psycopg2.connect(database='librosdb',user='victor',password='1325164',host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT')
