from django.conf.urls import url, include
from .views import register, student_main, instructor_main
from django.conf.urls import url, include

urlpatterns = [
    url(r'^student/$', student_main),
    url(r'^instructor/$', instructor_main),
    url(r'^register/$', register),
    url(r'^student/exam/', include('exam.urls')),
    url(r'^instructor/exam/', include('exam.urls')),
]