from django.conf.urls import url, include
from .views import exam_index,exam_delete,exam_detail,exam_update

urlpatterns = [

    url(r'^detail/', exam_detail),
    url(r'^index/$', exam_index),
    url(r'^update/$', exam_update),
    url(r'^delete/$', exam_delete),
]
