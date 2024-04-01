from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html')
        else:
            try:
                User.objects.get(email=email)
                messages.error(request, 'Contraseña incorrecta.')
            except User.DoesNotExist:
                messages.error(request, 'No existe una cuenta con ese correo electrónico.')
    return render(request, 'registration/login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 != password2:
            # Las contraseñas no coinciden
            return HttpResponseRedirect(reverse('registrarse'))
        User.objects.create_user(username=email, email=email, password=password1)
    return HttpResponseRedirect(reverse('index'))

def logout_view(request):
    logout(request)
    return redirect('index')
