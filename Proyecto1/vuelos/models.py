from django.db import models

# es posible asociar el modelo a una base de datos ya existente
# referencias https://uniwebsidad.com/libros/django-1-0

# algunas subclases de Field, para asociar los casos mas tipicos de datos para las bases de datos

# models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='')   el dato sera entero y aumenta automaticamente tal ocmo un SERIAL
# models.BigAutoField()             igual al interior per entero de 64 bits
# models.IntegerField()             entero
# models.BigIntegerField()          entero de 64 bits
# models.BinaryField(max_length=,**)              se le pueden asignar bytes,bytearrays o memoryview
# models.BooleanField()             suvalor por defecto es null, null=True
# models.CharField(max_length=)     char tipico
# models.TextField()                para texto muy extensos
# models.DateField(auto_now=False,auto_now_add=False,**)    auto_now, crea una fecha cuando un nuevo reocrd es añadido a la tabla, se ejecuta cuando se ahce Model.save(), al hacer update QuerySet.update() no se actualiza.
# models.DateTimeField()            igual a python datetime.datetime
# models.DecimalField(max_digits=5,decimal_places=4) digits es el tamaño total del numero
# models.Emailfield(max_length=*)   verifica si el valor es un email valido usando la funcion de python EmailValidator
# models.FileField(upload_to=*,max_length=*)
# models.FloatField()

# para la construccion de relaciones tambien hay algunos casos tipicos



# el modelo debe asociarse al proyecto en el archivo Protecto1/settings.py en INSTALLED_APPS se agrega el modelo de la app actual


# ya creado el modelo, se debe ejecutar el isguiente comando para crear la migracion, crear un archivo appname/migrations/xxxx_initial.py que creara el codigo sql
#   - python3 manage.py makemigrations
# con el isugiente ocmando s epeude ver el codigo sql que django va a usar para crear las tablas de la base de datos
#   - python3 manage.py sqlmigrate appname xxxx (numero del archivo app/migrations/initial_py) 
# ultimo paso basico importante configurar la base de datos proyecto/settings.py
# realizar la migracion
#   - python3 manage.py migrate 

# class vuelos(models.Model):  # Models.model con esto vuelos se convierte en una clase que pertenece a models.Model
#     id_origin = models.AutoField(primary_key=True,auto_created=True,serialize=False,verbose_name='pk_origin')
#     origin = models.CharField(max_length=64)
#     destination = models.CharField(max_length=64)
#     duration = models.IntegerField(null=True)

    # # para cualquier clase __str__ define cmo se debe ver un objeto de esta clase al ser impreso en pantalla
    # def __str__(self):
    #     #return f"{self.id_origin} - {self.origin} to {self.destination}" # este formato de string solo funciona en python3.7
    #     return str(self.id_origin) +' - '+ str(self.origin) +' to '+ str(self.destination) # python3

class airports(models.Model):
    id_airport = models.AutoField(primary_key=True,auto_created=True,serialize=False,verbose_name='pk_airport')
    codigo = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=64)

    def getCodigo(self):
        return self.codigo
    
    def getCiudad(self):
        return self.ciudad

    def __str__(self):
        return str(self.ciudad) + ' (' + str(self.codigo) + ')'


class vuelos(models.Model):
    id_vuelos = models.AutoField(primary_key=True,auto_created=True,serialize=False,verbose_name='pk_vuelo')
    id_origin = models.ForeignKey(airports,on_delete=models.CASCADE,related_name='fk_origen')
    id_destination = models.ForeignKey(airports,on_delete=models.CASCADE,related_name='fk_destino')
    duration = models.IntegerField(null=True)
   
    def __str__(self):
        return str(self.id_vuelos) +' - '+ str(self.id_origin) +' to '+ str(self.id_destination) # python3

# Django Shell para guardar datos
#   - python3 manage.py shell
# from vuelos.models import vuelos

# crear un registro en la tabla vuelos
#  - f = vuelos(origin="New York", destination="London", duration=415)
#  - f.save()

# restorna una lista llamada "queryList" pero no es observable a simple vista, se puede crear una funcion __str__ en le modelo para observar los datos
# vuelos.objects.all()[0]
# al crear la funcion __str__ los elemntos dentro de esta lista tendran el formato establecido por esta funcion
# crear un elemento en una tabla con foreign keys
# vuelo = vuelos(id_origin=airports.objects.all()[0],id_destination=airports.objects.all()[1],duration=415) el directamente asocia las primary keys de las tablas
# se puede listar cada columna como una instancia de la clase
# vuelo.id_origin, vuelo.duration, etc.
