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
    path('', views.index, name='index'),
    # path("specifics/<int:question_id>/", views.detail, name="detail"),

    # defino la ruta detail con el parametro question_id y le asigno la vista detail, con nombre detail
    # cambio el path para que lo codifique en la url
    path('<int:question_id>/', views.detail, name='detail'),

    # defino la ruta results con el parametro question_id y le asigno la vista results, con nombre results
    path('<int:question_id>/results/', views.results, name='results'),
    # defino la ruta vote con el parametro question_id y le asigno la vista vote, con nombre vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
