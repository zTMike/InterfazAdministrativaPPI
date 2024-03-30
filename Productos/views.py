from django.shortcuts import render
from .models import categoria, producto 
from django.http import HttpResponse
from django.template import Template, Context
from .views import *

# Create your views here.
def productos(request):

    productos = producto.objects.all()
    return render(request, 'Productos.html', {'productosquerry': productos})
