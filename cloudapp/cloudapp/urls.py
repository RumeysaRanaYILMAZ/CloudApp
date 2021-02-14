"""cloudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from user.views import register, login
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from main.views import main_view
from question.views import question_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^exam/', include('exam.urls', namespace='exam')),
    url(r'^main/', include('user.urls')),
    url(r'^question/', question_view),
    url(r'^$', main_view),
    url(r'^register/$', register, name="register"),
    url(r'^login/$', login, name="login")
]
