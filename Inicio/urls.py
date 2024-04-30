from django.urls import path,include
from .views import *
from Productos.views import productos
from Usuarios.views import register_view, logout_view,login_view


urlpatterns = [
    path('', index,name='index'),
    path('Productos/', productos,name='productos'),
    path('Nosotros/', nosotros,name='nosotros'),
    path('Contactenos/', contactenos,name='contactenos'),
    path('register/', register_view, name='registrer'),
    path('iniciarsesion/', iniciarsesion, name='iniciarsesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('',include('Usuarios.urls')),
    path('administrador/', administrador,name='administrador'),
    path('usuarios/', usuarios,name='usuarios'),
    path('Admin/Productos/', productosadmin,name='productosadmin'),
]
# Compare this snippet from Inicio/views.py: