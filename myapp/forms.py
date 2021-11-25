from django import forms
from myapp.models import Doctor, Patient

class DoctorForm(form.ModelForm):
  class Meta:
    model = Doctor
    fields = "__all__"

class PatientForm(form.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"