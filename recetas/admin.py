from django.contrib import admin
from .models import Perfil, Categoria, Receta, Favorito

admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(Receta)
admin.site.register(Favorito)