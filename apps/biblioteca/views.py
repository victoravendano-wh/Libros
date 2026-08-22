from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro
from django.core.mail import send_mail
from apps.biblioteca.forms import FormularioContacto

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

# def contactos(request):
#     errors = []
#     if request.method=='POST':
#         if not request.POST.get('asunto',''):
#             errors.append('Por favor introduce el asunto')
#         if not request.POST.get('mensaje',''):
#             errors.append('Por favor introduce un mensaje')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Por favor introduce una direccion de correo valida')
#         if not errors:
#             send_mail(request.POST['asunto'], request.POST['mensaje'], request.POST.get('email', 'noreply@example.com'), ['siteowner@example.com'],)
#             return HttpResponseRedirect('/contactos/gracias/')
#     return render(request, 'biblioteca/formulario-contactos.html', {'errors': errors, 'mensaje':request.POST.get('mensaje', ''), 'email':request.POST.get('email',''), 'asunto':request.POST.get('asunto','')})

def contactos(request):
    erorr=[]
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            clenad_data = form.cleaned_data
            send_mail(clenad_data['asunto'], clenad_data['mensaje'], clenad_data.get('email', 'noreply@example.com'), ['sitieowner@example.com'])
            return HttpResponse("""<H1>Se ha mandado tu mensaje</H1> <a href="../contacto/" class="btn btn-primary">Atras</a>""")
    else:
        form = FormularioContacto(initial={'asunto':'Adoto tu sitio!'})
    return render(request, 'biblioteca/formulario-contactos.html', {'form':form})            