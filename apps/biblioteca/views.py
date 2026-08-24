from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro
from django.core.mail import send_mail
from apps.biblioteca.forms import FormularioContacto, Formulario_libro
from django.http import Http404

from django.views.generic import DeleteView, UpdateView, CreateView, TemplateView, ListView, View


# Create your views here.

def landing(request): # mandamos nuestra landing a la raiz 🔥🔥🔥
    if request.method == 'GET':
        return render(request, "landing/index.html")
    else:
        return Http404("Pagina no encontrada")

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

# def contactos(request): #version primitiva
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
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            clenad_data = form.cleaned_data
            send_mail(clenad_data['asunto'], clenad_data['mensaje'], clenad_data.get('email', 'noreply@example.com'), ['sitieowner@example.com'])
            return HttpResponse("""<H1>Se ha mandado tu mensaje</H1> <a href="../contacto/" class="btn btn-primary">Atras</a>""")
    else:
        form = FormularioContacto(initial={'asunto':'Adoto tu sitio!'})
    return render(request, 'biblioteca/formulario-contactos.html', {'form':form})            

def nuevo(request):
    form = Formulario_libro()
    if request.method == "POST":
        form = Formulario_libro(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("app_libreria:busqueda")
    return render(request, 'biblioteca/formulario_libro.html', {'forms':form, 'titulo':'Nuevo'})


def editar(request, offset):
    
    libro = Libro.objects.get(id=offset)
    form = Formulario_libro(instance=libro)
    
    if request.method =="POST":
        form = Formulario_libro(request.POST, request.FILES, instance=libro )
        if form.is_valid():
            form.save()
            return redirect("app_libreria:busqueda")
    return render(request, 'biblioteca/formulario_libro.html', {'forms':form, 'titulo': 'Editar', "id":offset})

def eliminar(request, offset):
    libro = Libro.objects.get(id=offset)
    
    if request.method == "POST":
        
        libro.delete()
        return redirect("app_libreria:busqueda")
        
        
    return render(request, 'biblioteca/eliminar_libro.html', {'libro':libro}) 


class cbvresultado(View):
    error = []
    template_name = "biblioteca/formulario_buscar.html"
    def get(self,request, *args, **kwargs):          #Metodo GET
        if 'q' in request.GET:
            q = request.GET['q']
            if not q:
                self.error.append("No se han introducido parametros de busqueda")
            elif len(q)>20:
                self.error.append("Introduce un termino menor a 20 caracteres")
            else:
                libros = Libro.objects.filter(titulo__icontains=q)
                return render(request, 'biblioteca/resultado_busqueda.html', {'libros':libros, 'query':q})
        return render(request, 'biblioteca/formulario_buscar.html', {'error':self.error})
    def post(self, request, *args, **kwargs):
        return Http404("Pagina no encontrada")
    
    
class cbvlanding(View):
    template_name = 'landing/index.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        return Http404("Pagina no encontrada")