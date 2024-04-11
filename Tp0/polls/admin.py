from django.contrib import admin

# importo el modelo Question para poder registrarlo en el administrador
from .models import Question

# registro de la aplicación Question en el administrador esto permite 
# que se pueda administrar desde el panel de administración de Django
admin.site.register(Question)