# importo path que es el que voy a utilizar para definir las rutas de mi aplicación
from django.urls import path
# importo las vistas que voy a utilizar
from . import views

# defino la ruta de mi aplicación, en este caso la raíz, y le asigno la vista index, con nombre index
urlpatterns = [
    path('', views.index, name='index'),
]
