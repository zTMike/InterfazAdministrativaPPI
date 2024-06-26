from django.db import models
from django.contrib.auth.models import User
from Productos.models import producto
from Usuarios.models import Usuario

# Create your models here.
class orde_venta(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('A', 'Aprovado'),
        ('R', 'Rechazado'),
        ('E', 'Entregado'),
    ]

    id_orden_ord = models.AutoField(primary_key=True)
    id_usuario_ord = models.ForeignKey('Usuarios.Usuario', models.DO_NOTHING, db_column='id_usuario_ord')
    fecha_ord = models.DateField()
    total_ord = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    estado_ord = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')
   
   

    def __str__(self):
        return str(self.id_orden_ord)
    
class detalle_orden(models.Model):
    id_detalle_det = models.AutoField(primary_key=True)
    id_orden_det= models.ForeignKey(orde_venta,on_delete=models.PROTECT)
    id_producto_det = models.ForeignKey(producto,on_delete=models.PROTECT)
    cantidad_det = models.IntegerField()
    cantidad_entregada_det = models.IntegerField(default=0)
    precio_det = models.DecimalField(max_digits=9, decimal_places=2)
    subtotal_det = models.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        self.precio_def = self.id_producto_ven.precio_pro  # Asume que 'precio' es el campo del precio en el modelo 'producto'
        self.subtotal_def = self.precio_det * self.cantidad_def
        super().save(*args, **kwargs)

    
    def __str__(self):
        return str(self.id_detalle_det)