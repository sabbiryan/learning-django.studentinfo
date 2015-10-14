"""studentinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import core.views as coreviews

urlpatterns = [
    url(r'^$', coreviews.LandingView.as_view()),
    url(r'^student/$', coreviews.StudentListView.as_view(), name="student_list"),
    url(r'^student/(?P<pk>\d+)/detail/$', coreviews.StudentDetailView.as_view(), name="student_detail"),
    url(r'^create/$', coreviews.StudentCreateView.as_view(), name="student_create"),
    url(r'^student/(?P<pk>\d+)/update/$', coreviews.StudentUpdateView.as_view(), name="student_update"),
    url(r'^student/(?P<pk>\d+)/delete/$', coreviews.StudentDeleteView.as_view(), name="student_delete"),
]
