from django.shortcuts import render
# importo la libreria HttpResponse para poder devolver una respuesta
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    # aca traigo las ultimas 5 preguntas que se crearon ordenadas por fecha de publicacion
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # aca armo un string con las preguntas separadas por coma
    # el join es un metodo de los strings que une los elementos de una lista con un separador
    output = ", ".join([q.question_text for q in latest_question_list])
    # devuelvo la respuesta
    return HttpResponse(output)

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta
def detail(request, question_id):
    return HttpResponse("Estas mirando la pregunta %s." % question_id)

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta para indicar que se estan viendo los resultados
def results(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s." % question_id
    return HttpResponse(response % question_id)

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta para indicar que se esta votando
def vote(request, question_id):
    return HttpResponse("Estas votando la pregunta %s." % question_id)