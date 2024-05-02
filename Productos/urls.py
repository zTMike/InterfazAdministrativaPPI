from django.urls import path
from .views import *

urlpatterns = [ 
    path('admin/Productos/', productosadmin,name='productosadmin'),
    path('admin/categoriasadmin/', categoriasadmin,name='categoriasadmin'),
    path('admin/crearproducto/', crearproducto,name='crearproducto'),
    path('admin/crearCategoria/', crearcategoria,name='crearcategoria'),
    path('admin/productos/<int:id_producto_pro>/', producto_detalles, name='producto_detalles'),
    path('admin/categoria/<int:id_categoria_cat>/', categoria_detalles, name='categoria_detalles'),
    
]
