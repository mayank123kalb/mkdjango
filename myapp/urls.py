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
    path("appointments", views.appointments, name='appointments'),

    path("", views.IndexView.as_view(), name="index"),
    path("doctor/<int:pk>", views.DoctorDetailView.as_view(), name="doctor_detail"),
    path("patient/<int:pk>", views.PatientDetailView.as_view(), name="patient_detail"),
    path("patient/<int:pk>", views.PatientUpdateView.as_view(), name="patient_update"),
    path("patient/create", views.PatientCreateView.as_view(), name="patient_create"),
    

]