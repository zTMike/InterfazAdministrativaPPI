from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib.auth import logout
from django.contrib import messages
from django.db import connection
from django.http import Http404
from django.contrib.auth.hashers import make_password




# Create your views here.
def login_view(request):

    if request.method == 'POST':
        correo_usu = request.POST['email']
        contrasena_usu = request.POST['password']
        
    
    user = authenticate(request, username=correo_usu, password=contrasena_usu)
    
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        try:
            Usuario.objects.get(correo_usu=correo_usu)  
            messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Cuenta No Existe.')
    return redirect('iniciarsesion')

def register_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        documento = request.POST['documento']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
         # Comprueba si los campos están vacíos
        if not nombre or not apellido or not telefono or not documento or not email or not password or not password2:
            messages.error(request, 'Todos los campos son obligatorios')
            return redirect('registrarse')
        else:
            if password != password2:
                # Las contraseñas no coinciden
                messages.error(request, 'Las contraseñas no coinciden')
                return redirect('registrarse')
            else:
                
                username = request.POST['email']
                password= request.POST['password']
                Usuario.objects.create_user(id_usuario_usu=documento, correo_usu=username, contrasena_usu=password, nombre_usu=nombre, apellido_usu=apellido, telefono_usu=telefono)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                return redirect('index')

        # Aquí continúa tu lógica de registro...

    # Si el método no es POST, renderiza la página de registro normalmente
    return render(request, 'registration/register.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def usuarios(request):

   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios")
        column_names = [col[0] for col in cursor.description]
        usuariosquery = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'AdminUsuarios.html', {'usuarios': usuariosquery})

def productosadmin(request):

   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos_producto")
        column_names = [col[0] for col in cursor.description]
        productos = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'ProductosAdmin.html', {'productos': productos})

def iniciarsesion(request):
    return render(request, 'registration/login.html')

def registrarse(request):
    return render(request, 'registration/register.html')

def crear_usuario(request):
    if request.method == 'POST':
        id_usuario_usu =request.POST.get('id_usuario_usu')
        nombre = request.POST.get('nombre_usu')
        apellido = request.POST.get('apellido_usu')
        correo = request.POST.get('correo_usu')
        telefono = request.POST.get('telefono_usu')
        password = request.POST.get('password_usu')
        
        password = make_password(password)
        print(password)
        is_staff = 1 if request.POST.get('is_staff', False) == 'on' else 0
        is_active = 1
        if not nombre or not apellido or not correo or not telefono or not password:
            messages.error(request, 'Todos los campos son obligatorios')
            return redirect('crear_usuario')
        else:
            with connection.cursor() as cursor:
               cursor.execute("""INSERT INTO usuarios (id_usuario_usu, nombre_usu, apellido_usu, correo_usu, telefono_usu, password, is_active, is_staff)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            """, [id_usuario_usu, nombre, apellido, correo, telefono, password, is_active, is_staff])
                            
            messages.success(request, 'Usuario Creado Correctamente')
            return redirect('usuarios')
    return render(request, 'CrearUsuario.html')


def usuario_detalles (request, id_usuario_usu):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario_usu = %s", [id_usuario_usu])
        row = cursor.fetchone()
        if row is None:
            raise Http404("Usuario no existe")
        usuario = {
            'id_usuario_usu': row[0],
            'nombre_usu': row[1],
            'apellido_usu': row[2],
            'correo_usu': row[3],
            'telefono_usu': row[4],
            'password': row[5],
            'ultimologin': row[6],
            'is_active': row[7],
            'is_staff': row[8]
                
        }
        usuario['is_active'] = bool(int(usuario['is_active']))
        usuario['is_staff'] = bool(int(usuario['is_staff']))
        
    
    if request.method == 'POST':

        action = request.POST.get('action')
        if action == 'Actualizar':
            nombre = request.POST.get('nombre_usu')
            apellido = request.POST.get('apellido_usu')
            correo = request.POST.get('correo_usu')
            telefono = request.POST.get('telefono_usu')
            is_staff = 1 if request.POST.get('is_staff', False) == 'on' else 0
            is_active = 1 if request.POST.get('is_active', False) == 'on' else 0
            
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE usuarios 
                    SET nombre_usu = %s, 
                        apellido_usu = %s, 
                        correo_usu = %s, 
                        telefono_usu = %s,
                        is_staff = %s,
                        is_active = %s
                    WHERE id_usuario_usu = %s
                """, [nombre, apellido, correo, telefono, is_staff, is_active, id_usuario_usu])
                connection.commit()
                messages.error(request, 'Usuario Actualizado Correctamente')
            print('Usuario actualizado')

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id_usuario_usu = %s", [id_usuario_usu])
                row = cursor.fetchone()
                usuario = {
                    'id_usuario_usu': row[0],
                    'nombre_usu': row[1],
                    'apellido_usu': row[2],
                    'correo_usu': row[3],
                    'telefono_usu': row[4],
                    'password': row[5],
                    'ultimologin': row[6],
                    'is_active': row[7],
                    'is_staff': row[8]
                }
                
                usuario['is_active'] = bool(int(usuario['is_active']))
                usuario['is_staff'] = bool(int(usuario['is_staff']))
                print(usuario)
            return render(request, 'UsuarioDetalles.html', {'usuario': usuario})
        elif action == 'Eliminar':
            # Eliminar el usuario
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id_usuario_usu = %s", [id_usuario_usu])
                connection.commit()
                
            return redirect('usuarios')
    return render(request, 'UsuarioDetalles.html', {'usuario': usuario})