\# 🍳 Diario de Recetas



Aplicación web tipo blog desarrollada con Django, donde los usuarios pueden

registrarse, crear su perfil y publicar recetas de cocina con ingredientes,

pasos, tiempo de preparación y fotos.



\## 📌 Descripción del proyecto



\*\*Propósito:\*\* ofrecer un espacio colaborativo donde amantes de la cocina

puedan compartir y descubrir recetas caseras.



\*\*Problema que resuelve:\*\* centraliza recetas personales que normalmente

están dispersas en cuadernos, notas o mensajes, y permite organizarlas por

categoría y guardarlas como favoritas.



\*\*Usuario objetivo:\*\* cualquier persona que quiera compartir sus recetas

o buscar inspiración para cocinar.



\## ⚙️ Funcionalidades principales



\- \*\*Panel de administración (Django Admin):\*\* gestión de recetas, categorías,

&#x20; usuarios y perfiles desde `/admin/`.

\- \*\*Registro y autenticación de usuarios:\*\* los usuarios pueden crear una

&#x20; cuenta, iniciar sesión y cerrar sesión. Al registrarse, se crea

&#x20; automáticamente su perfil.

\- \*\*Publicación de recetas:\*\* los usuarios logueados pueden crear recetas

&#x20; con título, categoría, ingredientes, pasos, tiempo de preparación,

&#x20; porciones e imagen.

\- \*\*Validación de formularios:\*\* el título debe tener al menos 5 caracteres

&#x20; y el tiempo de preparación debe ser mayor a 0.

\- \*\*Sistema de favoritos:\*\* los usuarios pueden marcar recetas como

&#x20; favoritas y verlas en su perfil.

\- \*\*Perfil de usuario:\*\* cada usuario ve sus propias recetas publicadas

&#x20; y sus favoritos.



\## 🛠️ Tecnologías utilizadas



\- Python 3.14

\- Django 6.0.7

\- Pillow (manejo de imágenes)

\- Bootstrap 5 (estilos)

\- SQLite (base de datos en desarrollo)



\## 🚀 Instrucciones para ejecutar el proyecto localmente



\### Requisitos previos

\- Python 3.10 o superior instalado

\- pip



\### Pasos



1\. Clonar el repositorio:

git clone <URL-del-repositorio>

cd Python





2\. Crear y activar un entorno virtual:

python -m venv venv

venv\\Scripts\\activate # En Windows

source venv/bin/activate # En Mac/Linux



3\. Instalar las dependencias:

pip install -r requirements.txt



4\. Aplicar las migraciones:

python manage.py migrate



5\. Crear un superusuario (para acceder al panel admin):

python manage.py createsuperuser



6\. Ejecutar el servidor:

python manage.py runserver



7\. Abrir en el navegador:

&#x20;  - Sitio: `http://127.0.0.1:8000/`

&#x20;  - Panel admin: `http://127.0.0.1:8000/admin/`



\## 🌐 Despliegue



\*(Completar con la URL pública si desplegaste el proyecto en Render, 

Railway, PythonAnywhere, o con Ngrok. Si no lo desplegaste, explicá acá 

cómo se haría — por ejemplo: "Se desplegaría en Render conectando el 

repositorio de GitHub, configurando las variables de entorno DEBUG=False, 

ALLOWED\_HOSTS y ejecutando collectstatic durante el build".)\*



\## 📸 Capturas de pantalla



\*(Agregar acá capturas del panel admin, del registro, del listado de 

recetas, del detalle de una receta y del formulario de creación.)\*



\## 👤 Autor



TOMAS MONTOBBIO







