"""
URL configuration for Tp0 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# importo la libreria include para poder incluir las urls de mi aplicación
from django.urls import include,path

# La función include() permite hacer referencia a otros URLconfs.
# Cada vez que Django encuentra include() corta cualquier parte de la URL que coincide hasta ese punto y envía la cadena restante a la URLconf incluida para seguir el proceso.

urlpatterns = [
    # incluyo las urls de mi aplicación, en este caso la de polls que es la aplicación que cree
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
