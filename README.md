Estructura del Proyecto
  appfactory/ - Carpeta principal de la aplicación.
  
  models.py - Define los modelos de Producto, Cliente y Empleado.
  
  views.py - Contiene las vistas para manejar las solicitudes HTTP.
  
  urls.py - Define las rutas URL para la aplicación.
  
  templates/appfactory/ - Contiene las plantillas HTML.
  
    base.html - Plantilla base.
    index.html - Plantilla para la página de inicio.
    producto.html - Plantilla para gestionar productos.
    cliente.html - Plantilla para gestionar clientes.
    empleado.html - Plantilla para gestionar empleados.

Modelos
Los modelos definen la estructura de la base de datos para productos, clientes y empleados.

  Producto: 
    
    from django.db import models

    class Producto(models.Model):
        nombre = models.CharField(max_length=100)
        codigo = models.CharField(max_length=50, unique=True)
        stock = models.PositiveIntegerField()
    
        def __str__(self):
            return self.nombre

            
  Cliente: 
    
    from django.db import models

    class Cliente(models.Model):
        nombre = models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        dni = models.CharField(max_length=10, unique=True)
        email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
  
  
  Empleado:
    
    from django.db import models

    class Empleado(models.Model):
        nombre = models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        dni = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

Vistas
    
Las vistas manejan las solicitudes HTTP y renderizan las plantillas correspondientes.

Vista de Inicio 

La vista de inicio maneja la búsqueda de productos y muestra el resultado de la búsqueda.
  
    from django.shortcuts import render, redirect, get_object_or_404
    from .models import Producto, Cliente, Empleado
    
    def inicio(request):
        if request.method == 'POST':
            codigo = request.POST['codigoProductoBuscar']
            try:
                producto = Producto.objects.get(codigo=codigo)
            except Producto.DoesNotExist:
                return redirect('producto')
            return render(request, 'appfactory/index.html', {'producto': producto})
        return render(request, 'appfactory/index.html')

Vista de Producto

La vista de productos maneja la creación de nuevos productos.

    def producto(request):
        if request.method == 'POST':
            nombre = request.POST['nombreProducto']
            codigo = request.POST['codigoProducto']
            stock = request.POST['stockProducto']
            producto = Producto(nombre=nombre, codigo=codigo, stock=stock)
            producto.save()
            return redirect('inicio')
        return render(request, 'appfactory/producto.html')


Vista de Cliente

La vista de clientes maneja la creación de nuevos clientes.

    def cliente(request):
      if request.method == 'POST':
          nombre = request.POST['nombreCliente']
          apellido = request.POST['apellidoCliente']
          dni = request.POST['dniCliente']
          email = request.POST['emailCliente']
          cliente = Cliente(nombre=nombre, apellido=apellido, dni=dni, email=email)
          cliente.save()
          return redirect('inicio')
      return render(request, 'appfactory/cliente.html')


Vista de Empleado
        
La vista de empleados maneja la creación de nuevos empleados.

    def empleado(request):
        if request.method == 'POST':
            nombre = request.POST['nombreEmpleado']
            apellido = request.POST['apellidoEmpleado']
            dni = request.POST['dniEmpleado']
            empleado = Empleado(nombre=nombre, apellido=apellido, dni=dni)
            empleado.save()
            return redirect('inicio')
        return render(request, 'appfactory/empleado.html')


Plantillas

Las plantillas HTML se encuentran en el directorio templates/appfactory/.

base.html

        La plantilla base define la estructura común de todas las páginas, incluyendo el encabezado, el pie de página y el área principal de contenido.

index.html

        La plantilla para la página de inicio incluye la funcionalidad de búsqueda de productos y muestra el resultado de la búsqueda si el producto existe.

producto.html

        La plantilla para gestionar productos permite agregar nuevos productos a la base de datos.

cliente.html

        La plantilla para gestionar clientes permite agregar nuevos clientes a la base de datos.

empleado.html

        La plantilla para gestionar empleados permite agregar nuevos empleados a la base de datos.

