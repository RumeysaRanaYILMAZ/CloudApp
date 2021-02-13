from django.shortcuts import render
from exam.controllers import ExamController


def question_view(request):
    questions = ExamController('EXM2021020000').questions()
    return render(request, 'solvee.html', {'questions': questions})
