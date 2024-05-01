from django.urls import path
from .views import productosadmin

urlpatterns = [ 
    path('Admin/Productos/', productosadmin,name='productosadmin'),
]
