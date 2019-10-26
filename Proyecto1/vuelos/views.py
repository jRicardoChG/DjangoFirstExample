from django.shortcuts   import render       # viene por defecto a crear la vista
from django.http        import HttpResponse, Http404, HttpResponseRedirect #para manejar peticiones http
from .models            import vuelos, airports, pasajeros    # importo los models para poder obtener datos del mismo
from django.urls        import reverse
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
        "pasajeros" : vueloEspecifico.pasajerosq.all(),
        "no_pasajeros": pasajeros.objects.exclude(vuelos=vueloEspecifico).all() # elimino a todos los pasajeros que ya estan en este vuelo y retorno del modelo todos los demas
    }
    print(datos)
    return render(request,"vuelos/vuelo.html",datos)

def book(request,vuelo_id):
    try:
        idPasajero = int(request.POST["pasajero"])
        vueloRegistrar = vuelos.objects.get(pk=vuelo_id)
        pasajeroActual = pasajeros.objects.get(pk=idPasajero)
        print("hola has llegado hasta aca: ", idPasajero, vueloRegistrar, pasajeroActual )
    except KeyError:
        return render(request,"vuelos/error.html",{"message":"No selection"})
    except vuelos.DoesNotExist:
        return render(request,"vuelos/error.html",{"message":"No existe el vuelo"})
    except pasajeros.DoesNotExist:
        return render(request,"vuelos/error.html",{"message":"No existe el pasajero"})
    pasajeroActual.vuelos.add(vueloRegistrar)
    return HttpResponseRedirect(reverse("Vuelos",args=(vuelo_id,)))