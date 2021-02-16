from django.conf.urls import url, include
from .views import register, student_main, instructor_main
from django.conf.urls import url, include

app_name = "user"
urlpatterns = [
    url(r'^student/$', student_main, name='student'),
    url(r'^instructor/$', instructor_main, name='instructor'),
    url(r'^student/exam/', include('exam.urls')),
    url(r'^instructor/exam/', include('exam.urls')),
]