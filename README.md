# Blog Django

## Descripción

Blog creado con Django creado como parte de la Preentrega 8 del curso de Python. Incluye el proyecto `blog_project` y la aplicación `posts`, con templates HTML, herencia de plantillas y archivos estáticos (CSS).

**Requisito:** Python 3.12 o posterior, compatible con Django 6.1.2.

## Instalación

1. Clonar el repositorio de GitHub:

   `git clone https://github.com/JosiasPM/pre-entrega-curso-coderhouse.git`

2. Entrar en la carpeta del proyecto:

   `cd pre-entrega-curso-coderhouse`

3. Crear un entorno virtual:

   `python -m venv .venv`

4. Activar el entorno virtual:

   **Windows PowerShell:**

   `.\.venv\Scripts\Activate.ps1`

   **Linux/macOS:**

   `source .venv/bin/activate`

5. Instalar las dependencias:

   `python -m pip install -r requirements.txt`

## Ejecución

Iniciar el servidor con:

`python manage.py runserver`

Abrir en el navegador:

http://127.0.0.1:8000/

## Aplicación principal

La aplicación principal creada es `posts`.

## Páginas disponibles

- Inicio: http://127.0.0.1:8000/
- Acerca de: http://127.0.0.1:8000/acerca/

## Estructura de la app posts

- `posts/templates/posts/`: templates HTML (`base.html`, `inicio.html`, `acerca.html`)
- `posts/static/posts/css/`: archivo de estilos (`estilos.css`)