from django.conf.urls import url, include
from django.urls import path
from .views import exam_create, exam_index, exam_delete, exam_detail, exam_scores

app_name = "exam"
urlpatterns = [
    url(r'^create/$', exam_create, name="create"),
    url(r'^index/$', exam_index, name="index"),
    url(r'^(?P<exam_id>\w+)/delete/$', exam_delete, name="delete"),
    url(r'^(?P<exam_id>\w+)/scores/$', exam_scores, name="scores"),
    url(r'^(?P<exam_id>\w+)/', exam_detail, name="detail"),
]