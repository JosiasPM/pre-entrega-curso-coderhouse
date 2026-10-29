from django.shortcuts import render

# Muestra la página de inicio del blog.
def inicio(request):
    return render(request, 'posts/inicio.html')


# Muestra la página acerca del blog.
def acerca(request):
    return render(request, 'posts/acerca.html')