from django.db import models

# Create your models here.
class tipoUsuario(models.Model):
    id_tipoUsuario_tus = models.AutoField(primary_key=True)
    nombre_tus = models.CharField(max_length=50)
    descripcion_tus = models.TextField()
    def __str__(self):
        return self.nombre_tus
    
class usuario(models.Model):
    id_usuario_usu = models.IntegerField(primary_key=True)
    nombre_usu = models.CharField(max_length=50)
    apellido_usu = models.CharField(max_length=50)
    correo_usu = models.CharField(max_length=50)
    contrasena_usu = models.CharField(max_length=50)
    tipoUsuario_usu = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_usuario_usu) 
    
