
#pytest
import pytest
#Pruebas
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import connection
#importar vistas
from Productos.views import *
from Usuarios.views import *
from Ventas.views import *

#Base del request
@pytest.fixture
def rf():
    return RequestFactory()
#<-------------------TESTS DE CREAR CATEGORIA------------------->
@pytest.mark.categorias
@pytest.mark.parametrize("nombre_cat, descripcion_cat, expected_exception, expected_message", [
    ('Aseo', 'a'*256, ValueError, 'No se pudo crear Categoria'),
    ('', 'Utencilios de aseo', ValueError, 'Faltan Datos'),
    ('Aseo', '', ValueError, 'Faltan Datos'),
    ('Aseo', 'Utensilios de aseo', None, 'Categoria Creada Correctamente'),
    
])
@pytest.mark.django_db(transaction=True)
def test_Categoria(rf, nombre_cat, descripcion_cat, expected_exception, expected_message):
    request = rf.post('/crearcategoria/', {
        'nombre_cat': nombre_cat,
        'descripcion_cat': descripcion_cat,
    })
    

 # Añadir soporte para mensajes
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)\
    

    if expected_exception :
        with pytest.raises(expected_exception) as excinfo:
            crearcategoria(request)
        assert str(excinfo.value) == expected_message
    else:
        response = crearcategoria(request)
        assert request.custom_success == expected_message
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Categorias WHERE nombre_cat = %s", [nombre_cat])
    

#<-------------------TESTS DE CREAR PRODUCTO------------------->
@pytest.mark.productos
@pytest.mark.parametrize("nombre_pro, descripcion_pro, precio_pro, existencia_pro, categoria_pro_id, estado_pro, foto_pro, expected_exception, expected_message", [
    ('Escoba', 'Descripcion del Producto de Prueba', '1000', '10', '1', 'on', 'Lechuga.jpg', None, 'Producto Creado Correctamente'),
    ('Escoba', 'a'*256, '1000', '10', '1', 'on', 'Lechuga.jpg', ValueError, 'No se pudo crear el Producto'),
    ('', 'Descripcion del Producto de Prueba', '1000', '10', '1', 'on', 'Lechuga.jpg', ValueError, 'todos los campos son requeridos'),
    ('Escoba', '', '1000', '10', '1', 'on', 'Lechuga.jpg', ValueError, 'todos los campos son requeridos'),
    ('Escoba', 'Descripcion del Producto de Prueba', '', '10', '1', 'on', 'Lechuga.jpg', ValueError, 'todos los campos son requeridos'),
    ('Escoba', 'Descripcion del Producto de Prueba', '1000', '', '1', 'on', 'Lechuga.jpg', ValueError, 'todos los campos son requeridos'),
    ('Escoba', 'Descripcion del Producto de Prueba', '1000', '10', '', 'on', 'Lechuga.jpg', ValueError, 'todos los campos son requeridos'),
    ('Escoba', 'Descripcion del Producto de Prueba', '1000', '10', '1', 'on', '', ValueError, 'todos los campos son requeridos'),
    ('Escoba', 'Descripcion del Producto de Prueba', 'a', '10', '1', 'on', 'Lechuga.jpg', ValueError, 'Formato de número incorrecto'),
    
])
@pytest.mark.django_db(transaction=True)
def test_Producto(rf, nombre_pro, descripcion_pro, precio_pro, existencia_pro, categoria_pro_id, estado_pro, foto_pro, expected_exception, expected_message):
    request = rf.post('/crearproducto/', {
        'nombre_pro': nombre_pro,
        'descripcion_pro': descripcion_pro,
        'precio_pro': precio_pro,
        'stock_pro': existencia_pro,
        'categoria_pro': categoria_pro_id,
        'estado_pro': estado_pro,
        'foto_pro': foto_pro,
    },format='multipart')

    if foto_pro:
        foto = SimpleUploadedFile(name=foto_pro, content=b'', content_type='image/jpeg')
        request.FILES['foto_pro'] = foto

    request.user = AnonymousUser()

    # Añadir soporte para mensajes
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)

    if expected_exception:
        with pytest.raises(expected_exception) as excinfo:
            crearproducto(request)
        assert str(excinfo.value) == expected_message
    else:
        crearproducto(request)
        assert request.custom_success == expected_message

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Productos WHERE nombre_pro = %s", [nombre_pro])




#<-------------------TESTS DE CREAR USUARIO------------------->
@pytest.mark.usuarios
@pytest.mark.parametrize("id_usuario_usu, nombre_usu, apellido_usu, correo_usu, telefono_usu, password_usu, expected_exception, expected_message", [
    #Crea Usuarios Cambiar ID Y Correo
    ('4', 'Juan', 'Perez', 'juan.perez@example.com', '1234567890', 'password123', None, 'Usuario Creado Correctamente'),
    ('', 'Juan', 'Perez', 'juan.perez@example.com', '1234567890', 'password123', ValueError, 'todos los campos son obligatorios'),
    ('1', '', 'Perez', 'juan.perez@example.com', '1234567890', 'password123', ValueError, 'todos los campos son obligatorios'),
    ('1', 'Juan', '', 'juan.perez@example.com', '1234567890', 'password123', ValueError, 'todos los campos son obligatorios'),
    ('1', 'Juan', 'Perez', '', '1234567890', 'password123', ValueError, 'todos los campos son obligatorios'),
    ('1', 'Juan', 'Perez', 'juan.perez@example.com', '', 'password123', ValueError, 'todos los campos son obligatorios'),
    ('1', 'Juan', 'Perez', 'juan.perez@example.com', '1234567890', '', ValueError, 'todos los campos son obligatorios'),
    ('1234991936', 'Juan', 'Perez', 'juan.perez@example.com', '1234567890', 'password123', None, 'Usuario Ya existe'),
])
@pytest.mark.django_db(transaction=True)
def test_CrearUsuario(rf, id_usuario_usu, nombre_usu, apellido_usu, correo_usu, telefono_usu, password_usu, expected_exception, expected_message):
    # Crear una solicitud POST
    request = rf.post('/crearusuario/', {
        'id_usuario_usu': id_usuario_usu,
        'nombre_usu': nombre_usu,
        'apellido_usu': apellido_usu,
        'correo_usu': correo_usu,
        'telefono_usu': telefono_usu,
        'password_usu': password_usu,
    })
    request.user = AnonymousUser()

    # Añadir soporte para mensajes
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)

    if expected_exception:
        with pytest.raises(expected_exception) as excinfo:
            crear_usuario(request)
        assert str(excinfo.value) == expected_message
    else:
        response = crear_usuario(request)
        assert request.custom_success == expected_message
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Usuarios WHERE correo_usu = %s", [correo_usu])

#<-------------------TESTS DE CREAR VENTA------------------->
@pytest.mark.ventas
@pytest.mark.parametrize("carrito, expected_exception, expected_message", [
   ("[{'ID_DETALLE_DCAR': 1, 'CANTIDAD_DCAR': 2, 'PRECIO_DCAR': 18000.00, 'SUBTOTAL_DCAR': 36000.00, 'ID_PRODUCTO_DCAR': 1, 'ID_CARRITO_DCAR': 1, 'NOMBRE_PRODUCTO_DCAR': 'Huevos AAA'}]", ValueError, 'Venta Creada Correctamente'),
])
@pytest.mark.django_db(transaction=True)
def test_total_carrito(rf, carrito, expected_exception, expected_message):
    request = rf.post('/totalcarrito/', {'carrito': carrito})
    request.user = AnonymousUser()

    # Add support for messages
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)

    if expected_exception:
        with pytest.raises(expected_exception) as excinfo:
            total_carrito(request)
        assert str(excinfo.value) == expected_message
    else:
        response = total_carrito(request)
        assert response.status_code == 302  # Redirect to index
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM DetallesCarrito WHERE ID_DETALLE_DCAR = 1")

# @pytest.mark.login
# @pytest.mark.parametrize("correo_usu, password_usu, expected_exception, expected_message", [
#     ('He.fa.g.i@hotmail.com', '1234991936', ValueError, 'Login correcto'),
#     ('', '1234991936', ValueError, 'Correo o contraseña incorrectos'),
#     ('He.fa.g.i@hotmail.com', '', ValueError, 'Correo o contraseña incorrectos'),
#     ('', '', ValueError, 'Correo o contraseña incorrectos'),
# ])
# @pytest.mark.django_db(transaction=True)
# def test_login(rf, correo_usu, password_usu, expected_exception, expected_message):
#     request = rf.post('/login/', {
#         'email': correo_usu,
#         'password': password_usu,
#     })
    

#     # Add support for messages
#     setattr(request, 'session', 'session')
#     messages = FallbackStorage(request)
#     setattr(request, '_messages', messages)

#     if expected_exception:

#         with pytest.raises(expected_exception) as excinfo:
#             login(request)


#         assert str(excinfo.value) == expected_message
#     else:
#         response = login(request)
#         assert request.custom_success == expected_message








