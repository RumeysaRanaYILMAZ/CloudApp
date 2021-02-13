from django.shortcuts import render, HttpResponse


# Create your views here. #11.ders 13 14
def student_main(request):
    return HttpResponse('<b>keke student main</b>')


def instructor_main(request):
    return HttpResponse('<b>keke instructor main</b>')


def register(request):
    return render(request, 'register.html')
