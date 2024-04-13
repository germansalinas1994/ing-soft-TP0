from django.shortcuts import get_object_or_404, render
# importo la libreria HttpResponse para poder devolver una respuesta
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


from .models import Question

def index(request):
    # lo puedo hacer de 3 formas distintas


    # aca traigo las ultimas 5 preguntas que se crearon ordenadas por fecha de publicacion

    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # aca cargo el template que se va a utilizar

    # template = loader.get_template('polls/index.html')

    # armo el contexto que se va a utilizar en el template, seria el diccionario 
    # con el objeto que se va a utilizar en el template

    # context = {
    #     'latest_question_list': latest_question_list,
    # }

    # primera forma de devolver la respuesta con HttpResponse

    # devuelvo la respuesta, en lugar de hacerlo desde http lo hago desde render
    # return HttpResponse(template.render(context, request))

    # segunda forma de devolver la respuesta con render
    # renderiza el template con el contexto y devuelve la respuesta
    # return render(request, 'polls/index.html', context)

    # tercera forma de devolver la respuesta con render
    # renderiza el template con el contexto y devuelve la respuesta
    return render(request, 'polls/index.html', {"latest_question_list": latest_question_list})

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta
def detail(request, question_id):
    # primera forma de hacerlo
    # en lugar de hacerlo desde http lo hago desde render
    # return HttpResponse("Estas mirando la pregunta %s." % question_id)

    # segunda forma de hacerlo
    # try:
    #     # trata de traer la pregunta con el id que se pasa por parametro
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("La pregunta no existe")

    # tercera forma de hacerlo, utilizando get_object_or_404
    # trata de traer la pregunta con el id que se pasa por parametro y si no la encuentra devuelve un 404
    question = get_object_or_404(Question, pk=question_id)
    # renderiza el template con el contexto y devuelve la respuesta
    return render(request, 'polls/detail.html', {"question": question})

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta para indicar que se estan viendo los resultados
def results(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s." % question_id
    return HttpResponse(response % question_id)

# esta funcion recibe como parametro el question_id que se pasa por la url
# y devuelve un mensaje con el id de la pregunta para indicar que se esta votando
def vote(request, question_id):
    return HttpResponse("Estas votando la pregunta %s." % question_id)