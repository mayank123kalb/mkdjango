from django.db import models
from datetime import datetime
 

class Contact(models.Model):
	name = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	query =  models.TextField()
	date = models.DateField(default=datetime.now())



class Doctor(models.Model):
 doctor_name = models.CharField(max_length=30)
 registration_date = models.DateTimeField("date registered")
created_on = models.DateTimeField(auto_now_add=True)
speciality = models.CharField(max_length=20)

def __str__(self):
       return self.doctor_name



class Patient(models.Model):
 patient_name = models.CharField(max_length=30)
 created_on = models.DateTimeField(auto_now_add=True)
 registration_date = models.DateTimeField("date registered")
 waiting_status = models.BooleanField()

def __str__(self):
   return self.patient_name


@property
def is_waiting(self):
 return bool(self.waiting_status)