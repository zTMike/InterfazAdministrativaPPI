from django.urls import path
from Usuarios.views import *


urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('admin/logout/', logout_view, name='logout'),
    
]