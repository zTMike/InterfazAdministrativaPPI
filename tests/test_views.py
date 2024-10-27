import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from Productos.views import *

@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.parametrize("Nombre, Descripcion,Mensaje",[
    ('Categoría de Prueba', 'Descripción de la Categoría de Prueba','Categoria Creada Correctamente'),
    ('', 'Descripción de la Categoría de Prueba','No se pudo crear la categoria'),
    ('Categoría de Prueba', '','No se pudo crear la categoria'),
    (None, None,'No se pudo crear la categoria'),
])
@pytest.mark.django_db(transaction=True)
def test_Categoria(rf, Nombre, Descripcion, Mensaje):
    request = rf.post('/crearcategoria/', {# Se envía un POST con los datos de la categoría
        'nombre_cat': Nombre,# Nombre de la Categoría de Prueba
        'descripcion_cat': Descripcion,# Descripción de la Categoría de Prueba
    })
    request.user = AnonymousUser()# Se establece el usuario como anónimo
    with pytest.raises(ValueError) as excinfo:
        crearcategoria(request)# Se intenta crear la categoría
    assert Mensaje == str(excinfo.value)