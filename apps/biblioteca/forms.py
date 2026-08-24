from django import forms
from apps.biblioteca.models import Libro

class FormularioContacto(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    mensaje = forms.CharField(widget=forms.Textarea, max_length=200)
    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("Se requieren minimo 4 palabras!")
        return mensaje
    
    
class Formulario_libro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            "titulo",
            "autores",
            "editor",
            "fecha_publicada",
            "portada",
        ]
        labels = {
            "titulo": "Titulo",
            "autores": "Autores",
            "editor": "Editor",
            "fecha_publicada": "Fecha de publicacion",
            "portada": "Portada",
        }   
        # widgets = {
        #     "titulo": forms.TextInput(attrs={'class':'form-control d-block'}),
        #     "autores": forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox-list d-block'}),
        #     "editor": forms.RadioSelect(attrs={'class':'category-radio-group d-block'}),
        #     "fecha_publicada": forms.DateInput(),          
        # }  