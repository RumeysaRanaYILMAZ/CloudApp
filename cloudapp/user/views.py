from user.forms import UserForm
from django.shortcuts import redirect, render, HttpResponse
from user.controllers import UserController
from exam.controllers import ExamController
from django.views.decorators.csrf import csrf_exempt


# Create your views here. #11.ders 13 14
def student_main(request):
    mail = request.session['user']
    exams = ExamController.show_assigned_exams(mail)
    return render(request, 'student.html', {'exams': exams})


def instructor_main(request):
    return render(request, 'instructor.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        mail = request.POST['email']
        password = request.POST['password']
        loguser = UserController.login(mail, password)
        if loguser is None:
            return render(request, 'login.html')
        userform = UserForm.mail = mail
        if loguser.is_organizer:
            request.session['user'] = loguser.mail
            return redirect('../main/instructor', {'userform': userform})
        else:
            request.session['user'] = loguser.mail
            return redirect('../main/student', {'userform': userform})
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
