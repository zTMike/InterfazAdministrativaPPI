import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from Usuarios.views import *
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from Productos.views import *
from Ventas.views import *
from django.db import connection
from django.shortcuts import redirect
from datetime import datetime
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
import ast
from Usuarios.views import *
import random



@pytest.fixture
def rf():
    return RequestFactory()


#<----------------------TESTS DE CATEGORIAS-----------------------> OK
@pytest.mark.categorias
@pytest.mark.parametrize("nombre_cat, descripcion_cat, expected_status, expected_message", [
    # Caso exitoso: Todos los campos son válidos
    ('Categoria 1', 'Descripción de la Categoría 1', 302, 'Categoria Creada Correctamente'),
    
    # Caso fallido: Nombre de la categoría demasiado largo
    ('Categoria 1'*256, 'Descripción de la Categoría 1', 302, 'Error al crear la categoría'),
    
    # Caso fallido: Nombre de la categoría vacío
    ('', 'Descripción de la Categoría 1', 302, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Descripción de la categoría vacía
    ('Categoria 1', '', 302, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Ambos campos vacíos
    ('', '', 302, 'Todos los campos son obligatorios'),
])
@pytest.mark.django_db(transaction=True)
def test_CrearCategoria(rf, nombre_cat, descripcion_cat, expected_status, expected_message):
    # Crear una solicitud POST
    request = rf.post('/crearcategoria/', {
        'nombre_cat': nombre_cat,
        'descripcion_cat': descripcion_cat,
    })
    request.user = AnonymousUser()

    # Añadir soporte para mensajes
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)

    response = crearcategoria(request)
    assert response.status_code == expected_status
    for message in messages:
        print(f"Message: {message.message}")
    assert any(message.message == expected_message for message in messages)
    
    


#<----------------------TESTS DE PRODUCTOS-----------------------> OK
@pytest.mark.productos
@pytest.mark.parametrize("nombre_pro, descripcion_pro, precio_pro, stock_pro, estado_pro, foto_pro, categoria_pro, expected_exception, expected_message", [
    # Caso exitoso: Todos los campos son válidos
    ('Producto 1', 'Descripción del Producto 1', '100.00', '10', '1', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '1', None, 'Producto Creado Correctamente'),
    
    # Caso fallido: Nombre del producto vacío
    ('', 'Descripción del Producto 1', '100.00', '10', '1', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '1', None, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Descripción del producto vacía
    ('Producto 1', '', '100.00', '10', '1', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '1', None, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Precio del producto vacío
    ('Producto 1', 'Descripción del Producto 1', '', '10', '1', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '1', None, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Stock del producto vacío
    ('Producto 1', 'Descripción del Producto 1', '100.00', '', '1', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '1', None, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Estado del producto vacío
    ('Producto 1', 'Descripción del Producto 1', '100.00', '10', '', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '1', None, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Foto del producto vacía
    ('Producto 1', 'Descripción del Producto 1', '100.00', '10', '1', None, '1', None, 'Todos los campos son obligatorios'),
    
    # Caso fallido: Categoría del producto vacía
    ('Producto 1', 'Descripción del Producto 1', '100.00', '10', '1', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '', None, 'Todos los campos son obligatorios'),
    # Caso fallido: Nombre del producto muy largo
    ('Producto 1'*256, 'Descripción del Producto 1', '100.00', '10', '1', SimpleUploadedFile('foto.jpg', b'file_content', content_type='image/jpeg'), '1', None, 'Error al crear el producto'),
])
@pytest.mark.django_db(transaction=True)
def test_CrearProducto(rf, nombre_pro, descripcion_pro, precio_pro, stock_pro, estado_pro, foto_pro, categoria_pro, expected_exception, expected_message):
    # Crear una solicitud POST
    request = rf.post('/crearproducto/', {
        'nombre_pro': nombre_pro,
        'descripcion_pro': descripcion_pro,
        'precio_pro': precio_pro,
        'stock_pro': stock_pro,
        'estado_pro': estado_pro,
        'categoria_pro': categoria_pro,
    }, format='multipart')
    request.FILES['foto_pro'] = foto_pro
    request.user = AnonymousUser()

    # Añadir soporte para mensajes
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)

    response = crearproducto(request)
    if expected_exception:
        assert any(message.message == expected_message for message in messages)
    else:
        assert response.status_code == 302  # Redirección exitosa
        assert any(message.message == expected_message for message in messages)
    

#<----------------------TESTS DE VENTAS-----------------------> Ok


@pytest.mark.ventas
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("carrito, expected_message, expected_redirect", [
    # Caso 1: Carrito vacío
    ('[]', 'Carrito vacío', 'index'),
    # Caso 2: Carrito no encontrado
    ("[{'ID_DETALLE_DCAR': 1, 'CANTIDAD_DCAR': 1, 'PRECIO_DCAR': 100.00, 'SUBTOTAL_DCAR': 100.00, 'ID_PRODUCTO_DCAR': 1, 'ID_CARRITO_DCAR': 999, 'NOMBRE_PRODUCTO_DCAR': 'Producto 1'}]", 'Carrito no encontrado', 'index'),
    # Caso 3: Orden creada correctamente
    ("[{'ID_DETALLE_DCAR': 1, 'CANTIDAD_DCAR': 1, 'PRECIO_DCAR': 100.00, 'SUBTOTAL_DCAR': 100.00, 'ID_PRODUCTO_DCAR': 1, 'ID_CARRITO_DCAR': 1, 'NOMBRE_PRODUCTO_DCAR': 'Producto 1'}]", 'Orden creada correctamente', 'index'),
])
def test_total_carrito(rf, carrito, expected_message, expected_redirect):
  
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO CARRITOS (ID_CARRITO_CAR, TOTAL_CAR, ID_USUARIO_CAR) VALUES (1, 1, 1)")

    request = rf.post(('total_carrito'), {'carrito': carrito})
    request.user = AnonymousUser()

    # Añadir soporte para mensajes
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)

    response = total_carrito(request)
    assert response.status_code == 302  # Redirección exitosa
    assert response.url == reverse(expected_redirect)
    assert any(message.message == expected_message for message in messages)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM CARRITOS WHERE ID_CARRITO_CAR = 1")

 
#<----------------------TESTS DE USUARIOS-----------------------> Ok



User = get_user_model()

random_number = random.randint(1, 1000000)
@pytest.mark.usuarios
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("Nombre,Apellido,Telefono,DNI,Correo,Contraseña,ConfirmarContraseña, expected_message, expected_redirect", [
    # Caso 1: Usuario creado correctamente ok
    ('Hector', 'Diaz', '123456789', f'123{random_number}', f'He.fa.g.i{random_number}@hotmail.com', 'password123', 'password123', 'Usuario Creado Correctamente', 'index'),
    # Caso 2: Contraseñas no coinciden
    ( 'Hector', 'Diaz', '123456789', '12345678', 'He.fa.g.i1@hotmail.com', 'password123', 'password1234', 'Las contraseñas no coinciden', 'registrarse'),
    # Caso 3: Correo ya registrado
    ('Juan', 'Perez', '1234567890', '1', f'he.fa.g.i@hmotmail.com', 'password123', 'password123', 'Correo ya registrado', 'registrarse'),
    # Caso 4: Campos vacíos ok
    ( '', '', '', '', '', '', '', 'Todos los campos son obligatorios', 'registrarse'),
    # Caso 5: Correo inválido
    ('Hector', 'Diaz', '123456789', '12345678', 'correo', 'password123', 'password123', 'Correo inválido', 'registrarse')
])
def test_registrarse(rf, Nombre, Apellido, Telefono, DNI, Correo, Contraseña, ConfirmarContraseña, expected_message, expected_redirect):
    # Crear una solicitud POST
    request = rf.post(reverse('registrarse'), {
        'nombre': Nombre,
        'apellido': Apellido,
        'telefono': Telefono,
        'documento': DNI,
        'email': Correo,
        'password': Contraseña,
        'password2': ConfirmarContraseña,
    })

    # Añadir soporte para sesiones
    middleware = SessionMiddleware(lambda request: None)
    middleware.process_request(request)
    request.session.save()

    # Añadir soporte para mensajes
    setattr(request, '_messages', FallbackStorage(request))

    response = register_view(request)
    if expected_message:
        messages = list(request._messages)
        assert any(message.message == expected_message for message in messages)
        assert response.url == reverse(expected_redirect)




#<----------------------TESTS DE LOGIN-----------------------> 

User = get_user_model()

@pytest.mark.login
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize("email, password, expected_message, expected_redirect", [
    # Caso 1: Inicio de sesión exitoso
    ('he.fa.g.i@hmotmail.com', '1234', None, 'index'),
    # Caso 2: Contraseña incorrecta
    ('he.fa.g.i@hmotmail.com', 'wrongpassword', 'Contraseña incorrecta.', 'iniciarsesion'),
    # Caso 3: Cuenta no existe
    ('nonexistent@example.com', 'password123', 'Cuenta No Existe.', 'iniciarsesion'),
])
def test_login_view(rf, email, password, expected_message, expected_redirect):
    # Crear un usuario para las pruebas
    if email == 'testuser@example.com':
        User.objects.create_user(username=email, email=email, password='password123')

    # Crear una solicitud POST
    request = rf.post(reverse('iniciarsesion'), {
        'email': email,
        'password': password,
    })

    # Añadir soporte para sesiones
    middleware = SessionMiddleware(lambda request: None)
    middleware.process_request(request)
    request.session.save()

    # Añadir soporte para mensajes
    setattr(request, '_messages', FallbackStorage(request))

    response = login_view(request)
    if expected_message:
        messages = list(request._messages)
        assert any(message.message == expected_message for message in messages)
        assert response.url == reverse(expected_redirect)
    else:
        assert response.status_code == 302  # Redirección exitosa
        assert response.url == reverse(expected_redirect)






