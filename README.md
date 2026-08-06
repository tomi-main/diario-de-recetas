# 🍳 Diario de Recetas

Aplicación web tipo blog desarrollada con Django, donde los usuarios pueden
registrarse, crear su perfil y publicar recetas de cocina con ingredientes,
pasos, tiempo de preparación y fotos.

## 📌 Descripción del proyecto

**Propósito:** ofrecer un espacio colaborativo donde amantes de la cocina
puedan compartir y descubrir recetas caseras.

**Problema que resuelve:** centraliza recetas personales que normalmente
están dispersas en cuadernos, notas o mensajes, y permite organizarlas por
categoría y guardarlas como favoritas.

**Usuario objetivo:** cualquier persona que quiera compartir sus recetas
o buscar inspiración para cocinar.

## ⚙️ Funcionalidades principales

- **Panel de administración (Django Admin):** gestión de recetas, categorías,
  usuarios y perfiles desde `/admin/`.
- **Registro y autenticación de usuarios:** los usuarios pueden crear una
  cuenta, iniciar sesión y cerrar sesión. Al registrarse, se crea
  automáticamente su perfil.
- **Publicación de recetas:** los usuarios logueados pueden crear recetas
  con título, categoría, ingredientes, pasos, tiempo de preparación,
  porciones e imagen.
- **Validación de formularios:** el título debe tener al menos 5 caracteres
  y el tiempo de preparación debe ser mayor a 0.
- **Sistema de favoritos:** los usuarios pueden marcar recetas como
  favoritas y verlas en su perfil.
- **Perfil de usuario:** cada usuario ve sus propias recetas publicadas
  y sus favoritos.

## 🛠️ Tecnologías utilizadas

- Python 3.14
- Django 6.0.7
- Pillow (manejo de imágenes)
- Bootstrap 5 (estilos)
- SQLite (base de datos en desarrollo) / PostgreSQL (producción)
- Gunicorn + WhiteNoise (servidor de producción)

## 🚀 Instrucciones para ejecutar el proyecto localmente

### Requisitos previos
- Python 3.10 o superior instalado
- pip

### Pasos

1. Clonar el repositorio:
git clone https://github.com/tomi-main/diario-de-recetas.git
cd diario-de-recetas

2. Crear y activar un entorno virtual:
python -m venv venv
venv\Scripts\activate # En Windows
source venv/bin/activate # En Mac/Linux

3. Instalar las dependencias:
pip install -r requirements.txt

4. Aplicar las migraciones:
python manage.py migrate

5. Crear un superusuario (para acceder al panel admin):
python manage.py createsuperuser

6. Ejecutar el servidor:
python manage.py runserver

7. Abrir en el navegador:
   - Sitio: `http://127.0.0.1:8000/`
   - Panel admin: `http://127.0.0.1:8000/admin/`

## 🌐 Despliegue

**URL pública:** https://diario-de-recetas.onrender.com

El proyecto está desplegado en **Render** (plan gratuito), con la 
siguiente configuración:

- Web Service conectado directamente al repositorio de GitHub (deploy 
  automático con cada push a la rama `main`)
- Base de datos PostgreSQL gratuita provista por Render
- Gunicorn como servidor WSGI de producción
- WhiteNoise para servir los archivos estáticos (CSS, JS)
- Variables de entorno configuradas en Render: `SECRET_KEY`, `DEBUG=False`, 
  `DATABASE_URL`

### ⚠️ Nota sobre las imágenes en producción

El plan gratuito de Render no incluye almacenamiento persistente para archivos 
subidos por los usuarios (carpeta `media/`). Esto significa que las imágenes 
cargadas en las recetas se pierden cada vez que el servicio se reinicia 
(por ejemplo, tras un período de inactividad o un nuevo despliegue).

Para una solución en producción real, se recomendaría integrar un servicio de 
almacenamiento externo como **Cloudinary** o **AWS S3**, que mantiene los 
archivos disponibles de forma persistente independientemente del estado del 
servidor web.

## 📸 Capturas de pantalla

Las capturas de pantalla de todas las funcionalidades (panel admin, 
registro, login, listado de recetas, detalle, formulario de creación y 
perfil de usuario) están incluidas en la presentación de Google Slides 
de la entrega.

## 👤 Autor

Tomás Montobbio