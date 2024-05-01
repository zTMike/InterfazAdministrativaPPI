from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.db import connection


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            try:
                User.objects.get(email=email)
                messages.error(request, 'Contraseña incorrecta.')
            except User.DoesNotExist:
                messages.error(request, 'Cuenta No Existe.')
        return redirect('iniciarsesion')

def register_view(request):
    email = request.POST['email']
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']
         # Comprueba si los campos están vacíos
        if not email or not password or not password2:
            messages.error(request, 'Todos los campos son obligatorios')
            return redirect('registrarse')
        else:
            if password != password2:
                # Las contraseñas no coinciden
                messages.error(request, 'Las contraseñas no coinciden')
                return redirect('registrarse')
            else:
                # Las contraseñas coinciden
                email = request.POST['email']
                username = request.POST['email']
                password= request.POST['password']
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('index')

        # Aquí continúa tu lógica de registro...

    # Si el método no es POST, renderiza la página de registro normalmente
    return render(request, 'registration/register.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def usuarios(request):

   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM auth_user")
        column_names = [col[0] for col in cursor.description]
        usuariosquery = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'Usuarios.html', {'usuarios': usuariosquery})

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