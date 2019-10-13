
from django.shortcuts   import render
from django.http        import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hola soy el index de restaurante")

def home(request):
    return HttpResponse("Hola soy el Home de Restaurante")