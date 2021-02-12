from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Exam,Assignment,User

# Create your views here. #11.ders 13 14
def exam_detail(request):
    exam = get_object_or_404(Exam,id=9)

    return render(request,'instructor.html',{'exam':exam})
def exam_index(request):
    #if student if instructor ekle
    exams= Exam.objects.all()
    return render(request,'instructor.html',{'exams':exams})
def exam_delete(request):
    return HttpResponse('<b>keke delete</b>')
def exam_update(request):

    return HttpResponse('<b>keke update</b>')

