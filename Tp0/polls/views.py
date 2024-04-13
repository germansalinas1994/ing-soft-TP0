from django.shortcuts import render
# importo la libreria HttpResponse para poder devolver una respuesta
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    # aca traigo las ultimas 5 preguntas que se crearon ordenadas por fecha de publicacion
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # aca cargo el template que se va a utilizar
    template = loader.get_template('polls/index.html')

    # armo el contexto que se va a utilizar en el template, seria el diccionario 
    # con el objeto que se va a utilizar en el template
    context = {
        'latest_question_list': latest_question_list,
    }
    # devuelvo la respuesta, en lugar de hacerlo desde http lo hago desde render
    # return HttpResponse(template.render(context, request))

    # renderiza el template con el contexto y devuelve la respuesta
    return render(request, 'polls/index.html', context)

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