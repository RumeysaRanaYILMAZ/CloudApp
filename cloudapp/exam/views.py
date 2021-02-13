from exam.controllers import ExamController
from user.controllers import OrganizerController
from user.models import User
from question.models import Question
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Exam
from .forms import QuestionForm
import datetime
from django.views.decorators.csrf import csrf_exempt

userid = 'USR2021020001'
usermail = 'engin123@hotmail.com'


# Create your views here. #11.ders 13 14
def exam_detail(request):
    return HttpResponse('<b>keke delete</b>')


def exam_index(request):
    #if student if instructor ekle
    exams = Exam.objects.all()
    return render(request, 'instructor.html', {'exams': exams})


def exam_delete(request):
    return HttpResponse('<b>keke delete</b>')


def exam_update(request):
    return HttpResponse('<b>keke update</b>')


def exam_scores(request):
    #if student if instructor ekle
    exams = Exam.objects.all()
    return render(request, 'instructor.html', {'exams': exams})


@csrf_exempt
def exam_create(request):
    users = User.objects.filter(is_organizer=0)
    if request.method == 'POST':
        questnum = len(request.POST.getlist('question'))
        uscon = OrganizerController(usermail)
        date = datetime.datetime(2021, 12, 2)
        start = datetime.time(8, 30)
        end = datetime.time(10, 30)
        #print(request.POST)
        start_dt = datetime.datetime.combine(date.date(), start)
        end_dt = datetime.datetime.combine(date.date(), end)
        quiz = uscon.create_exam(request.POST['exam_name'], start_dt, end_dt)
        for i in range(questnum - 1):
            ExamController(quiz.id).question_add(
                request.POST.getlist('question')[i],
                request.POST.getlist('ans_1')[i],
                request.POST.getlist('ans_2')[i],
                request.POST.getlist('ans_3')[i],
                request.POST.getlist('ans_4')[i],
                request.POST.getlist('correct_answer')[i])
        for student in request.POST.getlist('students'):
            print(student)
            ExamController(quiz.id).assign(student)
    return render(request, 'createExam.html', {'users': users})
