from django.urls import path
from .views import *

urlpatterns = [
        path('Carrito/<int:usuario>/', carrito, name='carrito'),
        path('Agregar_carrito/', agregar_carrito,name='agregar_carrito'),
        path('total_carrito/', total_carrito,name='totalizar'),
        path('Ordenes/',ordenes,name='ordenes'),
        path('Ordenes/<int:id_orden>/',ordenes_detalles,name='Detalles_Orden'),
        path('ActualizarOrden/',actualizar_orden,name='actualizar_orden'),
        path('Eliminar_del_carrito/<int:item_id>/',eliminar_del_carrito,name='eliminar_del_carrito'),
        path('Detalles_orden/<int:id_orden>/',detalles_del_detalle,name='Detalles_detalles_orden'),
        path('actualizar_cantidad_entregada/<int:id_detalle>/', actualizar_cantidad_entregada, name='actualizar_cantidad_entregada'),
        path('cancelarpedido/<int:id_orden>/',cancelarpedido,name='cancelarpedido'),
        path('validar_cupon/<int:usuario>/', validar_cupon, name='validar_cupon'),


]
