from django.urls import path
from .views import *
from Productos.views import productos
from Usuarios.views import login_view
from Usuarios.views import register_view
from Usuarios.views import logout_view

urlpatterns = [
    path('', index,name='index'),
    path('Productos/', productos,name='productos'),
    path('Nosotros/', nosotros,name='nosotros'),
    path('Contactenos/', contactenos,name='contactenos'),
    path('cuentas/logout/', logout_view, name='logout'),
    path('cuentas/login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    


    
]
