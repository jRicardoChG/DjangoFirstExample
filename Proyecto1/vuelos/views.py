from django.shortcuts   import render       # viene por defecto a crear la vista
from django.http        import HttpResponse,Http404 #para manejar peticiones http
from .models      import vuelos,airports    # importo los models para poder obtener datos del mismo
import logging
import sys
# Create your views here.
# este es el archivo central, lo cree asi: debo isntalar Django en mi pc
# creo un proyecto nuevo llamado Proyecto1 que tendra muchas aplciaciones dentro
#           - django-admin startproject nombreDeseadoParaElProyecto
# Proyecto1 crea una carpeta interior tambien llamada Proyecto1 (igual al nombre del proyecto) dentro de esta estaran las diferentes aplicaciones que se crearan
# creo la primera app
#           - python3 manage.py startapp nombreAppDeseada
# puedo crear muchas apps que haran parte del proyecto
# el archivo Views.py es elarchivo principal que controla la data entre modelo y templates y recibe las peticiones http.
# los templates deben estar en cada appname/templates/archivo.html

logger = logging.getLogger(__name__)
#primera funcion de ruta, pero hay uqe asociarla a una ruta usando el archivo url.py de la app

def index(request):
    datos = {"vuelosDisponibles":vuelos.objects.all()}
    return render(request,"vuelos/index.html",datos)

def home(request):
    return HttpResponse("Hola este es el home de vuelos!")

def saludo(request):
    return HttpResponse("Hola soy una subcarpeta")

# cuando solicito un elelmento especifico .objects me traE LO QUE LA FUNCION __STR__ TIENE POR OBLIGACION MOSTRAR y sus columnas si quiero
# vuelo_id se definio en el archivo urls.py como el integer que va en la url pidiendo el vuelo
def Vuelos(request,vuelo_id):
    try:
        vueloEspecifico = vuelos.objects.get(pk=vuelo_id)
    except:
        raise Http404("el vuelo no existe")
    datos = {
        "vuelo" : vueloEspecifico,
        "pasajeros" : vueloEspecifico.pasajerosq.all()
    }
    print(datos["vuelo"])
    return render(request,"vuelos/vuelo.html",datos)


