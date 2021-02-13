from question.models import Question
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Exam, User


# Create your views here. #11.ders 13 14
def exam_detail(request):
    exam = get_object_or_404(Exam, id='EXM2021020000')

    return render(request, 'instructor.html', {'exam': exam})


def exam_index(request):
    #if student if instructor ekle
    exams = Exam.objects.all()
    return render(request, 'instructor.html', {'exams': exams})


def exam_delete(request):
    return HttpResponse('<b>keke delete</b>')


def exam_update(request):

    return HttpResponse('<b>keke update</b>')


class ExamView:
    id = None
    name = None
    organizer = None
    questions = None
    start = None
    end = None

    def __init__(self, examid):
        self.id = examid
        selected_exam = Exam.objects.filter(pk=examid).get()
        self.name = selected_exam.name
        instructor = User.objects.filter(pk=selected_exam.organizer)
        self.organizer = instructor
        self.questions = Question.objects.filter(exam_id=examid)
        self.start = selected_exam.start_time
        self.end = selected_exam.end_time