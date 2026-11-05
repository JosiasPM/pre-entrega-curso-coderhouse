from django.shortcuts import render
from .models import Post

# Muestra la página de inicio del blog.
def inicio(request):
    return render(request, 'posts/inicio.html')


# Muestra la página acerca del blog.
def acerca(request):
    return render(request, 'posts/acerca.html')

# Muestra la lista de publicaciones.
def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, 'posts/lista_posts.html', {'posts': posts})