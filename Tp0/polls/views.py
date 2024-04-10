from django.shortcuts import render
# importo la libreria HttpResponse para poder devolver una respuesta
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo, esta es mi primera vista en Django!")
