from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/stat', login_view, name='login'),
    path('admin/logout/', logout_view, name='logout'),
    path('admin/Usuarios/', usuarios,name='usuarios'),
    path('admin/usuario/<int:id_usuario_usu>/', usuario_detalles, name='usuario_detalles'),
    path('admin/usuario/crear_usuario/', crear_usuario, name='crear_usuario'),
    
]