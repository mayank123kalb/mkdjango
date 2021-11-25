from django.contrib import admin
from myapp.models import Contact
from myapp.models import Doctor, Patient
  
# Register your models here.
admin.site.register(Contact)
admin.site.register(Doctor)
admin.site.register(Patient)

