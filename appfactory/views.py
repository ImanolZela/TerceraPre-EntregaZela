from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def inicio(request):
    if request.method == 'POST':
        codigo = request.POST['codigoProductoBuscar']
        try:
            producto = Producto.objects.get(codigo=codigo)
        except Producto.DoesNotExist:
            return redirect('producto')
        return render(request,"appfactory/index.html", {'producto' : producto})
    return render(request, "appfactory/index.html")

def producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombreProducto']
        codigo = request.POST['codigoProducto']
        stock  = request.POST['stockProducto']
        
        producto = Producto(nombre=nombre, codigo=codigo, stock=stock)
        producto.save()
        return redirect('inicio') 
    return render(request, "appfactory/producto.html")

def cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombreCliente']
        apellido = request.POST['apellidoCliente']
        dni = request.POST['dniCliente']
        email = request.POST['emailCliente']
        
        cliente = Cliente(nombre=nombre, apellido=apellido, dni=dni, email=email)
        cliente.save()
    return render(request, "appfactory/cliente.html")

def empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombreEmpleado']
        apellido = request.POST['apellidoEmpleado']
        dni = request.POST['dniEmpleado']
        
        empleado = Empleado(nombre=nombre, apellido=apellido, dni=dni)
        empleado.save()
    return render(request, "appfactory/empleado.html")
