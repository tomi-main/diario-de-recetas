from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receta/<int:pk>/', views.receta_detalle, name='receta_detalle'),
    path('receta/nueva/', views.crear_receta, name='crear_receta'),
    path('receta/<int:pk>/favorito/', views.toggle_favorito, name='toggle_favorito'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='recetas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
]