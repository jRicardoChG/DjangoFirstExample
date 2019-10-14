from django.shortcuts   import render       # viene por defecto a crear la vista
from django.http        import HttpResponse #para manejar peticiones http

# Create your views here.
# este es el archivo central, lo cree asi: debo isntalar Django en mi pc
# creo un proyecto nuevo llamado Proyecto1 que tendra muchas aplciaciones dentro
#           - django-admin startproject nombreDeseadoParaElProyecto
# Proyecto1 crea una carpeta interior tambien llamada Proyecto1 (igual al nombre del proyecto) dentro de esta estaran las diferentes aplicaciones que se crearan
# creo la primera app
#           - python3 manage.py startapp nombreAppDeseada
# puedo crear muchas apps que haran parte del proyecto
# el archivo Views.py es elarchivo principal que controla la data entre modelo y templates y recibe las peticiones http.



#primera funcion de ruta, pero hay uqe asociarla a una ruta usando el archivo url.py de la app
def index(request):
    return HttpResponse("Hello, world!")

def home(request):
    return HttpResponse("Hola este es el home de vuelos!")

def saludo(request):
    return HttpResponse("Hola soy una subcarpeta")