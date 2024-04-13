# importo path que es el que voy a utilizar para definir las rutas de mi aplicación
from django.urls import path
# importo las vistas que voy a utilizar
from . import views

# defino la ruta de mi aplicación, en este caso la raíz, y le asigno la vista index, con nombre index
urlpatterns = [
    path('', views.index, name='index'),
    # defino la ruta detail con el parametro question_id y le asigno la vista detail, con nombre detail
    path('<int:question_id>/', views.detail, name='detail'),
    # defino la ruta results con el parametro question_id y le asigno la vista results, con nombre results
    path('<int:question_id>/results/', views.results, name='results'),
    # defino la ruta vote con el parametro question_id y le asigno la vista vote, con nombre vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
