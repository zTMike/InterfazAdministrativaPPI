from django.shortcuts import render
from django.db import connection

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactenos(request):
    return render(request, 'Contactenos.html')

def nosotros(request):
    return render(request, 'Nosotros.html')

def iniciarsesion(request):
    return render(request, 'registration/login.html')

def registrarse(request):
    return render(request, 'registration/register.html')

def administrador(request):
    return render(request, 'Administrador.html')


def usuarios(request):

   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM auth_user")
        column_names = [col[0] for col in cursor.description]
        usuariosquerry = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'Usuarios.html', {'usuarios': usuariosquerry})

   
def productosadmin(request):

   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos_producto")
        column_names = [col[0] for col in cursor.description]
        productos = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        print(productos)  # Imprime en consola
        return render(request, 'ProductosAdmin.html', {'productos': productos})



