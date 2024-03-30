from django.contrib import admin
from .models import orde_venta, detalle_orden

@admin.register(orde_venta)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden_ord', 'id_usuario_ord', 'fecha_ord', 'total_ord', 'estado_ord')
    ordering = ('id_orden_ord',)
    search_fields = ('id_orden_ord','id_usuario_ord__id_usuario_usu')  # Buscará por el id del usuario
    list_display_links = ()
    list_filter = ('fecha_ord','estado_ord')
    exclude = ('id_orden_ord', 'id_usuario_ord', 'fecha_ord', 'total_ord',)

    def has_add_permission(self, request):
        return False
    

    def get_actions(self, request):
        # No permite acciones de selección múltiple
        return None

@admin.register(detalle_orden)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_det', 'id_orden_det', 'id_producto_det', 'cantidad_det', 'precio_det', 'subtotal_det')
    ordering = ('id_detalle_det',)
    search_fields = ('id_orden_det__id_orden_ord',)  # Buscará por el id de la orden
    list_display_links = None
    exclude = ('id_detalle_det', 'id_orden_det', 'id_producto_det', 'cantidad_det', 'precio_det', 'subtotal_det')

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        # No permite acciones de selección múltiple
        return None