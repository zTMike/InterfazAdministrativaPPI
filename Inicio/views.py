from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactenos(request):
    return render(request, 'Contactenos.html')


def nosotros(request):
    return render(request, 'Nosotros.html')

