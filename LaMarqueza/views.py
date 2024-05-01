from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def contactenos(request):
    return render(request, 'Contactenos.html')

def nosotros(request):
    return render(request, 'Nosotros.html')



def administrador(request):
    return render(request, 'Administrador.html')

