from django.contrib import admin
from .models import categoria, producto
from django.contrib.auth.models import User, Group
#admin.site.unregister(User)
#admin.site.unregister(Group)
# Register your models here.
@admin.register(categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria_cat', 'nombre_cat', 'descripcion_cat')
    ordering = ('id_categoria_cat',)
    search_fields = ('nombre_cat','id_categoria_cat')
    list_display_links = ('nombre_cat', 'descripcion_cat')
    list_filter = ('nombre_cat',)  # Agrega un filtro por 'nombre_cat'
    list_per_page = 10  # Muestra 10 registros por página
    #exclude = ('descripcion_cat',)Excluir campos de la vista de edición
   

    def get_actions(self, request):
        # No permite acciones de selección múltiple
        return None
    
@admin.register(producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto_pro', 'nombre_pro', 'descripcion_pro', 'existencia_pro', 'precio_pro','categoria_pro','estado')
    ordering = ('id_producto_pro',)
    search_fields = ('nombre_pro','id_producto_pro')
    list_display_links = ('nombre_pro', 'descripcion_pro')
    list_filter = ('categoria_pro__nombre_cat',)
    list_editable = ('estado',)

    

    def get_actions(self, request):
        # No permite acciones de selección múltiple
        return None