# este archivo debe crearse para asociar las urls propias de esta aplicacion, para mantener el orden

from django.urls import path

from . import views         #importa views desde la carpeta vuelos (nombre de la app)

urlpatterns = [             # se indican todas las urls soportadas por la aplicacion
    path("",views.index,name="indexa"),   #index es la funcion ruta que se creo anteriormente en views, "" indica que es la ruta vacia o por defecto
    path("<int:vuelo_id>",views.Vuelos), # ejemplo ruta que recibe carpeta de entrada
    path("homeVuelos",views.home),
    path("homeVuelos/saludo",views.saludo)

]
