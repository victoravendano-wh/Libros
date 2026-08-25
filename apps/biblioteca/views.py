from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro
from django.core.mail import send_mail
from apps.biblioteca.forms import FormularioContacto, Formulario_libro
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from django.views.generic import DeleteView, ListView, View


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
            messages.success(request, "Nuevo libro agregado a la libreria")
            return redirect("app_libreria:listar")
    return render(request, 'biblioteca/formulario_libro.html', {'forms':form, 'titulo':'Nuevo'})


def editar(request, offset):
    
    libro = Libro.objects.get(id=offset)
    form = Formulario_libro(instance=libro)
    
    if request.method =="POST":
        form = Formulario_libro(request.POST, request.FILES, instance=libro )
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado correctamente")
            return redirect("app_libreria:listar")
    return render(request, 'biblioteca/formulario_libro.html', {'forms':form, 'titulo': 'Editar', "id":offset})

def eliminar(request, offset):
    libro = Libro.objects.get(id=offset)
    
    if request.method == "POST":
        
        libro.delete()
        messages.warning(request, "Se ha eliminado un libro de la libreria")
        return redirect("app_libreria:listar")
        
        
    return render(request, 'biblioteca/eliminar_libro.html', {'libro':libro}) 

def listar(request):
    lista = Libro.objects.all().order_by('id')
    if request.method == "GET":
        return render(request, 'biblioteca/lista.html', {'lista':lista})
    
    raise Http404("Pagina no encontrada")


class Cbvresultado(View):
    error = []
    template_name = "cbvbiblioteca/formulario_buscar.html"
    def get(self,request, *args, **kwargs):          #Metodo GET
        if 'q' in request.GET:
            q = request.GET['q']
            if not q:
                self.error.append("No se han introducido parametros de busqueda")
            elif len(q)>20:
                self.error.append("Introduce un termino menor a 20 caracteres")
            else:
                libros = Libro.objects.filter(titulo__icontains=q)
                return render(request, 'cbvbiblioteca/resultado_busqueda.html', {'libros':libros, 'query':q})
        return render(request, 'cbvbiblioteca/formulario_buscar.html', {'error':self.error})
    def post(self, request, *args, **kwargs):
        return Http404("Pagina no encontrada")
    
    
class Cbvlanding(View):
    template_name = 'cbvbiblioteca/index.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        return Http404("Pagina no encontrada")
    
    
class Cbvcontactos(View):
    
    def post(self, request, *args, **kwargs):
        form = FormularioContacto(request.POST)
        if form.is_valid():
            clenad_data = form.cleaned_data
            send_mail(clenad_data['asunto'], clenad_data['mensaje'], clenad_data.get('email', 'noreply@example.com'), ['sitieowner@example.com'])
            return HttpResponse("""<H1>Se ha mandado tu mensaje</H1> <a href="../../cbv/contacto/" class="btn btn-primary">Atras</a>""")
        else:
            return render(request, 'cbvbiblioteca/formulario-contactos.html', {'form':form})
    def get(self, request, *args, **kwargs):
        form = FormularioContacto(initial={'asunto':'Adoto tu sitio!'})
        return render(request, 'cbvbiblioteca/formulario-contactos.html', {'form':form})

class Cbvnuevo(View):
    form = Formulario_libro()
    def get(self, request, *args, **kwargs):
        return render(request, 'cbvbiblioteca/formulario_libro.html', {'forms':self.form, 'titulo':'Nuevo'})
    def post(self, request, *args, **kwargs):
        form = Formulario_libro(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Nuevo libro agregado a la libreria")
            return redirect("app_libreria:cbv_listar")
        else:
            return render(request, 'cbvbiblioteca/formulario_libro.html', {'forms':form, 'titulo':'Nuevo'})
        

class Cbveditar(View):
        
    
    def get(self, request, *args, **kwargs):
        libro = get_object_or_404(Libro, id=self.args[0])
        form = Formulario_libro(instance=libro)
        return render(request, 'cbvbiblioteca/formulario_libro.html', {'forms':form, 'titulo': 'Editar', "id":self.args[0]})  
        
        
    def post(self, request, *args, **kwargs):
        libro = get_object_or_404(Libro, id=self.args[0])
        form = Formulario_libro(request.POST, request.FILES, instance=libro )
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado correctamente")
            return redirect("app_libreria:cbv_listar")
        else:
            return render(request, 'cbvbiblioteca/formulario_libro.html', {'forms':form, 'titulo': 'Editar', "id":self.args[0]})
          
    
class Cbveliminar(DeleteView):
    model = Libro
    template_name = 'cbvbiblioteca/eliminar_libro.html'
    success_url = reverse_lazy('app_libreria:cbv_listar')
    
    def post(self, *args, **kwargs):
        messages.warning(self.request, "Se ha eliminado un libro de la libreria")
        return super().post(self, *args, **kwargs)
    
class Cbvlistar(ListView):
    model = Libro
    template_name = 'cbvbiblioteca/lista.html'
    context_object_name = "lista"
    def get_queryset(self):
        return Libro.objects.all().order_by("id")