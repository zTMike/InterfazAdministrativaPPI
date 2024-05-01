from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, correo_usu, contrasena_usu=None, **extra_fields):
        if not correo_usu:
            raise ValueError('El correo es obligatorio')
        user = self.model(correo_usu=self.normalize_email(correo_usu), **extra_fields)
        user.set_password(contrasena_usu)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_usu, contrasena_usu=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo_usu, contrasena_usu, extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario_usu = models.IntegerField(primary_key=True)
    nombre_usu = models.CharField(max_length=50)
    apellido_usu = models.CharField(max_length=50)
    correo_usu = models.EmailField(unique=True)
    contrasena_usu = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_usu'
    REQUIRED_FIELDS = ['nombre_usu', 'apellido_usu']

    def str(self):
        return str(self.id_usuario_usu)
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    @property
    def is_superuser(self):
        return self.is_staff
    
    
