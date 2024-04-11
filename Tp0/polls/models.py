import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

# creo dos modelos para mi aplicación, uno para las preguntas y otro para las opciones


# la clase Question tiene dos atributos, question_text y pub_date, que son de tipo CharField y DateTimeField respectivamente.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # el método __str__ devuelve el texto de la pregunta
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# la clase Choice tiene una relación con la clase Question,
# por lo que se debe definir un campo ForeignKey que haga referencia a la clase Question.
# al poner el on delete en cascada se indica que si se elimina una pregunta se eliminan 
# todas las opciones asociadas a esa pregunta
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # la funcion __str__ devuelve el texto de la opción
    def __str__(self):
        return self.choice_text