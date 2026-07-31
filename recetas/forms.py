from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Receta


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'categoria', 'ingredientes', 'pasos', 'tiempo_preparacion', 'porciones', 'imagen']

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return titulo

    def clean_tiempo_preparacion(self):
        tiempo = self.cleaned_data['tiempo_preparacion']
        if tiempo <= 0:
            raise forms.ValidationError("El tiempo debe ser mayor a 0 minutos.")
        return tiempo