from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='myapp'),
    path("about", views.about, name='about'),
    path("info", views.info, name='info'),
    path("contact", views.contact, name='contact'),
    path("create", views.create, name='create'),
    path("recent", views.recent, name='recent'),
    path("workspace", views.workspace, name='workspace'),


  ]
  