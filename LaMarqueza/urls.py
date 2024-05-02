"""
URL configuration for LaMarqueza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Productos.views import *
from Usuarios.views import *
from LaMarqueza.views import *


urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', index,name='index'),
    path('',include('Usuarios.urls')),
    path('',include('Productos.urls')),
    path('Productos/', productos,name='productos'),
    path('Nosotros/', nosotros,name='nosotros'),
    path('Contactenos/', contactenos,name='contactenos'),
    path('Register/', register_view, name='registrer'),
    path('Iniciarsesion/', iniciarsesion, name='iniciarsesion'),
    path('Registrarse/', registrarse, name='registrarse'),
    path('Administrador/', administrador,name='administrador'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
