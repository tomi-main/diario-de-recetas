from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Receta, Categoria, Favorito
from .forms import RegistroForm, RecetaForm


def home(request):
    recetas = Receta.objects.all().order_by('-fecha_publicacion')
    return render(request, 'recetas/home.html', {'recetas': recetas})


def receta_detalle(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/receta_detalle.html', {'receta': receta})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'recetas/registro.html', {'form': form})


@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            return redirect('receta_detalle', pk=receta.pk)
    else:
        form = RecetaForm()
    return render(request, 'recetas/receta_form.html', {'form': form})


@login_required
def perfil(request):
    recetas = Receta.objects.filter(autor=request.user)
    favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'recetas/perfil.html', {'recetas': recetas, 'favoritos': favoritos})


@login_required
def toggle_favorito(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    favorito, creado = Favorito.objects.get_or_create(usuario=request.user, receta=receta)
    if not creado:
        favorito.delete()
    return redirect('receta_detalle', pk=receta.pk)