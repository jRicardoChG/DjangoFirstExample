from django.contrib import admin
from vuelos.models  import airports,vuelos,pasajeros # importo los modelso apra poder adicionar data desde la pagina admin

# Register your models here.
admin.site.register(airports)
admin.site.register(vuelos)
admin.site.register(pasajeros)
# para pdoer loguarse a la pagina de super usuario, se debe crear un super usuario en el proyecto
# python manage.py createsuperuser
# desde aca puedo ver datos de manera rapido y agregar datos como lo hacia desde la terminal de manage.py shell