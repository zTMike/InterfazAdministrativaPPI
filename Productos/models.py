from django.db import models

# Create your models here.
class categoria (models.Model):
    id_categoria_cat = models.AutoField(primary_key=True)
    nombre_cat = models.CharField(max_length=50)
    descripcion_cat = models.TextField()
    def __str__(self):
        texto= "{0}"
        return texto.format(self.nombre_cat)



class producto (models.Model):
    id_producto_pro = models.AutoField(primary_key=True)
    nombre_pro = models.CharField(max_length=50)
    descripcion_pro = models.TextField()
    categoria_pro = models.ForeignKey(categoria, on_delete=models.CASCADE)
    existencia_pro = models.IntegerField()
    precio_pro = models.IntegerField()
    foto=models.ImageField(upload_to='productos', null=True, blank=True)
    estado=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre_pro
    def delete(self, *args, **kwargs):
        self.foto.delete(save=False)
        super().delete(*args, **kwargs)