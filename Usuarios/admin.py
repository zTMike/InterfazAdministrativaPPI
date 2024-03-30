from django.contrib import admin
from .models import tipoUsuario, usuario

# Register your models here.
@admin.register(usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario_usu', 'nombre_usu', 'apellido_usu', 'correo_usu', 'contrasena_usu', 'tipoUsuario_usu')
    ordering = ('id_usuario_usu',)
    search_fields = ('nombre_usu','id_usuario_usu',)
    list_display_links = ('nombre_usu', 'apellido_usu')
    list_filter = ('tipoUsuario_usu__nombre_tus',)
    exclude = ('id_usuario_usu',)  # Excluir campos de la vista de edición
    

    def get_actions(self, request):
        # No permite acciones de selección múltiple
        return None

@admin.register(tipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_tipoUsuario_tus', 'nombre_tus', 'descripcion_tus')  # Agrega 'descripcion_tus' a 'list_display'
    ordering = ('id_tipoUsuario_tus',)
    search_fields = ('nombre_tus','id_tipoUsuario_tus')
    list_display_links = ('nombre_tus', 'descripcion_tus')
    list_filter = ('nombre_tus',)
    
    def get_actions(self, request):
        # No permite acciones de selección múltiple
        return None