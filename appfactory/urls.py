from django.urls import path

from appfactory.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('pagina-producto/', producto, name='producto'),
    path('pagina-cliente/', cliente, name='cliente'),
    path('pagina-empleado/', empleado, name='empleado'),
]