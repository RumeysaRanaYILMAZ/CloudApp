from django.shortcuts import render
from .controllers import QuestionController

def question_view(request):

    questions=QuestionController.questions(1)
    return render(request,'solvee.html', {'questions':questions})
