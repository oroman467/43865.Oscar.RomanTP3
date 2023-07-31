from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *


def index(request):
    return render(request, "aplicacion/base.html")

def compras(request):
    return render(request, "aplicacion/compras.html")

def ventas(request):
    return render(request, "aplicacion/ventas.html")

def alquileres(request):
    ctx = {"alquileres": Alquiler.objects.all()} 
    return render(request, "aplicacion/alquileres.html", ctx)

def alquilerForm(request):
    if request.method == "POST":
        alquiler = Alquiler(nombre=request.POST['nombre'], tipo=request.POST['tipo'], precio=request.POST['precio'])
        alquiler.save()
        return HttpResponse ("Se grabo con exito el Alquiler!")
    return render(request, "aplicacion/alquilerForm.html")

def alquilerForm2(request):
    if request.method == "POST":
        miForm=AlquilerForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            alquiler=Alquiler(nombre=informacion['nombre'], tipo=informacion['tipo'], precio=informacion['precio'])
            alquiler.save()
            return render(request, "aplicacion/base.html")
    else:
       
        miForm = AlquilerForm()
    
    return render(request, "aplicacion/alquilerForm2.html", {"form": miForm})


def equipos(request):
    ctx = {"equipos": Equipo.objects.all()} 
    return render(request, "aplicacion/equipos.html", ctx)

def equipoForm(request):
    if request.method == "POST":
        equipo = Equipo(nombre=request.POST['nombre'], tipo=request.POST['tipo'])
        equipo.save()
        return HttpResponse ("Se grabo con exito el Equipo!")
    return render(request, "aplicacion/equipoForm.html")

def equipoForm2(request):
    if request.method == "POST":
        miForm=EquipoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            equipo=Equipo(nombre=informacion['nombre'], tipo=informacion['tipo'])
            equipo.save()
            return render(request, "aplicacion/base.html")
    else:
       
        miForm = EquipoForm()
    
    return render(request, "aplicacion/equipoForm2.html", {"form": miForm})


def buscarPrecio(request):
    return render(request, "aplicacion/buscarPrecio.html")

def buscar2(request):
    if request.GET['precio']:
        precio=request.GET['precio']
        alquileres=Alquiler.objects.filter(precio__icontains=precio)
        return render(request, 
                       "aplicacion/resultadosPrecio.html",
                      {"precio":precio, "alquileres":alquileres})
    return HttpResponse("No se ingresaron datos!")
    

