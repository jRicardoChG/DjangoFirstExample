# este archivo debe crearse para asociar las urls propias de esta aplicacion, para mantener el orden

from django.urls import path

from . import views         #importa views desde la carpeta vuelos (nombre de la app)

urlpatterns = [             # se indican todas las urls soportadas por la aplicacion
    path("",views.index),   #index es la funcion ruta que se creo anteriormente en views, "" indica que es la ruta vacia o por defecto
    path("homeVuelos",views.home),
    path("homeVuelos/saludo",views.saludo)

]
