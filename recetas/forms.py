from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Receta


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Nombre de usuario'
        })
        self.fields['username'].help_text = None
        self.fields['email'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'tu@email.com'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Contraseña'
        })
        self.fields['password1'].help_text = None
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Repetir contraseña'
        })
        self.fields['password2'].help_text = None


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'categoria', 'ingredientes', 'pasos', 'tiempo_preparacion', 'porciones', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ej: Tarta de manzana'
            }),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'ingredientes': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5, 'placeholder': 'Un ingrediente por línea'
            }),
            'pasos': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 6, 'placeholder': 'Un paso por línea'
            }),
            'tiempo_preparacion': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Minutos'
            }),
            'porciones': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Cantidad de porciones'
            }),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

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


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Nombre de usuario'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Contraseña'
        })