from django.db import models

# Create your models here.


class Editor(models.Model):
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(blank=True, verbose_name="E-mail")
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor,  on_delete=models.CASCADE)
    fecha_publicada = models.DateField(null=True, blank=True)
    portada = models.ImageField(upload_to='portadas', blank=True)
    def __str__(self):
        return self.titulo
    