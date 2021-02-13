from django.shortcuts import render


def main_view(request):

    if not request.user.is_authenticated:
        context = {'isim': 'giriş yapmamış admine kek buğriş'}
    else:
        context = {'isim': 'giriş yapmış admine kek buğriş'}
    return render(request,'scores.html')
