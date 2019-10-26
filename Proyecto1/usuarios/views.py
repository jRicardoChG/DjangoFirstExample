from django.contrib.auth import authenticate,login,logout    # libreria django que contiene  un modelo de usuarios, con las fucniones authenticate,login, logout
from django.http import HttpResponse,HttpPresponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated: # retorno true si el usuario esta loggeado 
        return render(request,"usuarios/login.html",{"message":None}) # si no esta logeado se redirije a la pagina principal
    context = {
        "user":request.user
    } 
    return render(request,"usuarios/user.html",context)


def login_view(request):
    username = request.POST["nombreUsuario"]
    password = request.POST["contrasena"]
    usuario = authenticate(request,username=nombreUsuario,password=contrasena) # verifica si el usuario existe y retorna un objeto con los daots de usuario
    if usuario is not None:
        login(request,user) # si el usuario existe lo loguea en el sistema de autenticacion
        return HttpPresponseRedirect(reverse("index"))
    else:
        return render(request,"usuarios/login.html",{"message":"Credenciales Invalidas"})

def Logout_view(request):
    logout(request) # desloguea al usuario
    return render(request, "usuarios/login.html",{"message":"Te has deslogueado"})






