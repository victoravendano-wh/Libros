from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro
from django.core.mail import send_mail


# Create your views here.

def resultado(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append("No se han introducido parametros de busqueda")
        elif len(q)>20:
            error.append("Introduce un termino menor a 20 caracteres")
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'biblioteca/resultado_busqueda.html', {'libros':libros, 'query':q})
    return render(request, 'biblioteca/formulario_buscar.html', {'error':error})

def contactos(request):
    errors = []
    if request.method=='POST':
        if not request.POST.get('asunto',''):
            errors.append('Por favor introduce el asunto')
        if not request.POST.get('mensaje',''):
            errors.append('Por favor introduce un mensaje')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor introduce una direccion de correo valida')
        if not errors:
            send_mail(request.POST['asunto'], request.POST['mensaje'], request.POST.get('email', 'noreply@example.com'), ['siteowner@example.com'],)
            return HttpResponseRedirect('/contactos/gracias/')
    return render(request, 'biblioteca/formulario-contactos.html', {'errors': errors})
