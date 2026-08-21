from django.contrib import admin

# Register your models here.

from apps.biblioteca.models import Editor, Autor, Libro

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email')
    search_fields = ('nombre', 'apellidos')
    
class LibroAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'editor', 'fecha_publicada')
    list_filter = ('fecha_publicada',)
    date_hierarchy = 'fecha_publicada'
    ordering = ('-fecha_publicada',)
    fields = ('titulo', 'autores', 'editor', 'portada')
    filter_horizontal = ("autores",)
    raw_id_fields = ('editor',)

admin.site.register(Editor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
