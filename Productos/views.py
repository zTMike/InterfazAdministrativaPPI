from django.shortcuts import render
from .views import *
from django.db import connection

# Create your views here.
def productos(request):

   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos_producto")
        column_names = [col[0] for col in cursor.description]
        productos = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'Productos.html', {'productosquerry': productos})

def productosadmin(request):

   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos_producto")
        column_names = [col[0] for col in cursor.description]
        productos = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'ProductosAdmin.html', {'productos': productos})