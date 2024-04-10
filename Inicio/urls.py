from django.urls import path
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
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('admin/logout/', logout_view, name='logout'),

    


    
]
# Compare this snippet from Inicio/views.py: