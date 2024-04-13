# importo path que es el que voy a utilizar para definir las rutas de mi aplicación
from django.urls import path
# importo las vistas que voy a utilizar
from . import views


# defino la aplicacion a la que pertenecen las rutas, agrego el espacio de nombres
# defino la ruta de mi aplicación, en este caso la raíz, y le asigno la vista index, con nombre index
# con esto si tengo mas de una view detail puedo distinguir a cual me refiero
# es como los controllers de laravel o los controladores de spring o .net core
app_name = "polls"
urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
