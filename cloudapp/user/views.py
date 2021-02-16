from user.forms import UserForm
from django.shortcuts import redirect, render, HttpResponse
from user.controllers import UserController
from exam.controllers import ExamController
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_main(request):
    if request.method == 'GET':
        print(request.GET)
    mail = request.session['user']
    exams = ExamController.show_assigned_exams(mail)

    return render(request, 'student.html', {'exams': exams})


def instructor_main(request):
    mail = request.session['user']
    exams = ExamController.show_created_exams(mail)
    return render(request, 'instructor.html', {'exams': exams})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        mail = request.POST['email']
        password = request.POST['password']
        loguser = UserController.login(mail, password)
        if loguser is None:
            request.session['logged'] = 0
            return render(request, 'login.html')
        userform = UserForm.mail = mail
        if loguser.is_organizer:
            request.session['user'] = loguser.mail
            request.session['logged'] = 1
            request.session['organizer'] = 1
            request.session['name'] = loguser.name + " " + loguser.surname
            return redirect('../main/instructor', {'userform': userform})
        else:
            request.session['user'] = loguser.mail
            request.session['logged'] = 1
            request.session['organizer'] = 0
            request.session['name'] = loguser.name + " " + loguser.surname
            return redirect('../main/student', {'userform': userform})
    return render(request, 'login.html')


@csrf_exempt
def logout(request):
    request.session['user'] = None
    request.session['logged'] = 0
    request.session['organizer'] = None
    request.session['name'] = None
    return render(request, 'main.html')


def register(request):
    return render(request, 'register.html')
