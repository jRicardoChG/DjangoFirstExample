from django.contrib import admin
from vuelos.models  import airports,vuelos,pasajeros # importo los modelso apra poder adicionar data desde la pagina admin


class PasajeroEnLinea(admin.StackedInline):
    model = pasajeros.vuelos.through
    extra = 1

class VueloAdmin(admin.ModelAdmin):
    inlines = [PasajeroEnLinea]

class PasajeroAdmin(admin.ModelAdmin):
    filter_horizontal = ("vuelos",)

# Como vuelos no tiene una relacion directa con pasajeros por la tabla de rompimiento, al incluir el modelo pasajeros a admin, este no puede anadir vuelos a pasajeros directamente. Por esto se crea la clase PasajerosEnLinea de tipo StackedInline, que permite anadir nuevas relaicones entre objetos. PasajerosEnlinea representa el lugar en admin para poder modificar a los pasajeros

# pasajeros.vuelos.through hace referencia ala tabla de rompimiento, al igualar model a esta tabla se asocia a la clase PasajeroEnLinea
# extra = 1 define cuantos pasajeros se pueden editar al mismo tiempo

# VueloAdmin es una nueva clase de tipo ModelAdmin, y permite una serie de configuraciones epseciales para editar pasajeros, estas configuraciones se permiten al registrarla con vuelos en la linea admin.site.register(vuelos,VuelosAdmin)
# inlines contienen todas las modificaciones enlinea para la apgina admin, en este caso Admin solo tiene la clase PasajeroEnLinea

# filter_horizontal ayuda a manipular en que viaje esta el pasajero, simplemente anade un elemento UI a la pagina admin para facilitar el anadir o eliminar vuelos en los cuales esta el pasajero



# Register your models here.
admin.site.register(airports)
admin.site.register(vuelos,VueloAdmin)
admin.site.register(pasajeros, PasajeroAdmin)
# para pdoer loguarse a la pagina de super usuario, se debe crear un super usuario en el proyecto
# python manage.py createsuperuser
# desde aca puedo ver datos de manera rapido y agregar datos como lo hacia desde la terminal de manage.py shell


