# Blog Django

## Descripción

Blog creado con Django como parte de la Preentrega 9 del curso de Python. Incluye el proyecto `blog_project` y la aplicación `posts`, con templates HTML, herencia de plantillas, archivos estáticos (CSS), modelos y panel de administración.

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

   `.venv\Scripts\Activate.ps1`

   **Linux/macOS:**

   `source .venv/bin/activate`

5. Instalar las dependencias:

   `python -m pip install -r requirements.txt`

## Base de datos

Aplicar las migraciones:

`python manage.py migrate`

## Panel de administración

Crear un superusuario:

`python manage.py createsuperuser`

Iniciar el servidor:

`python manage.py runserver`

Acceder al panel de administración:

http://127.0.0.1:8000/admin/

Desde el panel se pueden crear, editar y administrar publicaciones.

Se creó un superusuario para acceder al panel de administración y se cargaron 3 publicaciones de prueba con diferentes estados: borrador, publicado y archivado.

La base de datos SQLite (db.sqlite3) se mantiene de forma local y no se incluye en el repositorio. La base de datos puede recrearse ejecutando las migraciones del proyecto.

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
- Posts: http://127.0.0.1:8000/posts/
- Administración: http://127.0.0.1:8000/admin/

La página Posts muestra las publicaciones cuyo estado es Publicado, ordenadas desde la más reciente.

## Estructura de la app posts

- `posts/models.py`: modelo Post.
- `posts/admin.py`: configuración del panel de administración.
- `posts/views.py`: vistas de la aplicación.
- `posts/urls.py`: rutas de la aplicación.
- `posts/templates/posts/`: templates HTML (`base.html`, `inicio.html`, `acerca.html`, `lista_posts.html`).
- `posts/static/posts/css/`: archivo de estilos (`estilos.css`).