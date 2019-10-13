"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# aca debo asociar los archivos url.py de cada una de las aplciaciones que yo cree. porque django solo reconoce este archivo de urls
# para ejecutar el proyecto 
#           - python3 manage.py runserver
# al tener varias aplciaciones hay uqe tener en cuenta
# se debe definir un path "" (vacio) par auqe sea el path por defecto al cual se va a asociar el path de este archivo
# es decir, si tengo la app = vuelos con un path vacio a la funcion index()
# si defino en este archivo path("vuelos/",include("vuelos.urls")), index() estara asociado a la ruta localhost:8000/vuelos/
# todas las rutas dependeran de este /vuelos/ para dirigirse a esta app en particular
# ejemplo localhost:8000/vuelos/homeVuelos/saludo 

from django.contrib     import admin
from django.urls        import path,include        # el archivo original no tiene el include

urlpatterns = [
    path("resta/",include("restaurante.urls")),
    path("vuelos/",include("vuelos.urls")),
    path('admin/', admin.site.urls)
]


