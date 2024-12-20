from django.urls import path
from .views import *

urlpatterns = [ 
    path('admin/Productos/', productosadmin,name='productosadmin'),
    path('admin/categoriasadmin/', categoriasadmin,name='categoriasadmin'),
    path('admin/crearproducto/', crearproducto,name='crearproducto'),
    path('admin/crearCategoria/', crearcategoria,name='crearcategoria'),
    path('admin/productos/<int:id_producto_pro>/', producto_detalles, name='producto_detalles'),
    path('admin/categoria/<int:id_categoria_cat>/', categoria_detalles, name='categoria_detalles'),
    path('admin/producto/resena', agregar_resena,name='agregar_resena'),
    path('admin/producto/resena/<int:id_resena_re>/', eliminar_resena, name='eliminar_resena'),
    path('admin/productos/favoritos/<int:id_producto_pro>/', agregar_favoritos, name='agregar_favoritos'),
    path('admin/crearCupon/', crearcupon, name='cupones'),
    path('admin/Cupones/', cuponessadmin,name='cuponessadmin'),
    path('cupones/eliminar/<int:id_cupon>/', eliminar_cupon, name='eliminar_cupon'),





 

]
