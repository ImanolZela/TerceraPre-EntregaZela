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

Vista de Producto

    La vista de productos maneja la creación de nuevos productos.

Vista de Cliente

    La vista de clientes maneja la creación de nuevos clientes.

Vista de Empleado
        
        La vista de empleados maneja la creación de nuevos empleados.

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

