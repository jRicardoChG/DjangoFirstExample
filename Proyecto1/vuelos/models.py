from django.db import models

# algunas subclases de Field, para asociar los casos mas tipicos de datos para las bases de datos

# models.AutoField()                el dato sera entero y aumenta automaticamente tal ocmo un SERIAL
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


# Create your models here.

class vuelos(Models.model):                         # Models.model con esto vuelos se convierte en una clase que pertenece a models.model
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
