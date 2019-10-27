from django.contrib.auth import authenticate,login,logout    # libreria django que contiene  un modelo de usuarios, con las fucniones authenticate,login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# no olvidar en el archivo settings.py del proyecto incluir la app usuarios.apps.UsuariosConfig en InstaledApps

# Create your views here.

def index(request):
    if not request.user.is_authenticated: # retorno true si el usuario esta loggeado 
        return render(request,"usuarios/login.html",{"message":None}) # si no esta logeado se redirije a la pagina de logueo
    context = {
        "user":request.user
    } 
    return render(request,"usuarios/userMain.html",context)

def login_view(request):
    nombreUsuario = request.POST["nombreUsuario"]
    contrasena = request.POST["contrasena"]
    usuario = authenticate(request,username=nombreUsuario,password=contrasena) # verifica si el usuario existe y retorna un objeto con los daots de usuario
    if usuario is not None:
        login(request,usuario) # si el usuario existe lo loguea en el sistema de autenticacion
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"usuarios/login.html",{"message":"Credenciales Invalidas"})

def logout_view(request):
    logout(request) # desloguea al usuario
    return render(request, "usuarios/login.html",{"message":"Te has deslogueado"})


# para registrar a un usuario hay uqe hacerlo con la base de datos

#  from django.contrib.auth.models import User
#  usuario = User.objects.create_user("alicia","alicia@email.com","alice12345")
#   

