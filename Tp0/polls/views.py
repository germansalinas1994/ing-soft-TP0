from django.shortcuts import render
# importo la libreria HttpResponse para poder devolver una respuesta
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo, esta es mi primera vista en Django!")

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta
def detail(request, question_id):
    return HttpResponse("Estas mirando la pregunta %s." % question_id)

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta para indicar que se estan viendo los resultados
def results(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta para indicar que se esta votando
def vote(request, question_id):
    return HttpResponse("Estas votando la pregunta %s." % question_id)