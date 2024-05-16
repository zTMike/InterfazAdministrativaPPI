from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone



class UsuarioManager(BaseUserManager):
    def create_user(self,id_usuario_usu, correo_usu, contrasena_usu=None, **extra_fields):
        if not correo_usu:
            raise ValueError('El correo es obligatorio')
        user = self.model(id_usuario_usu=id_usuario_usu,correo_usu=self.normalize_email(correo_usu), **extra_fields)
        user.set_password(contrasena_usu)
        user.save()
        return user

    def create_superuser(self,id_usuario_usu, correo_usu, contrasena_usu=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(id_usuario_usu ,correo_usu, contrasena_usu, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario_usu = models.PositiveIntegerField(primary_key=True)
    nombre_usu = models.CharField(max_length=50)
    apellido_usu = models.CharField(max_length=50)
    correo_usu = models.EmailField(max_length=50, unique=True)
    telefono_usu = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128)
    last_login = models.DateField(blank=True, null=True)
    is_active = models.CharField(max_length=1 , default='1')
    is_staff = models.CharField(max_length=1 ,default='0')
    

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_usu'
    REQUIRED_FIELDS = ['nombre_usu', 'apellido_usu','id_usuario_usu' ]
    class Meta:
            db_table = 'usuarios'
    def __str__(self):
        return str(self.id_usuario_usu)
    
    

    @property
    def is_superuser(self):
        return self.is_staff
    @is_superuser.setter
    def is_superuser(self, value):
        self.is_staff = value
    
    
