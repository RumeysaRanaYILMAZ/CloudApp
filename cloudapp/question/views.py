from django.shortcuts import render
from exam.controllers import ExamController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def question_view(request):
    examView = ExamController('1').exam_show()
    questions=examView.questions
    if request.method == 'POST':
        print(request.POST)


    return render(request, 'solvee.html', {'questions': questions})


