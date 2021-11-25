from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from .models import Doctor, Patient

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
	context = {
	'variable1': "hey",
	'variable2': "its me"

	}
	return render(request, 'index.html', context)
	
def about(request):
	return HttpResponse("My about page")


def info(request):
	return HttpResponse("information of my app page")


def contact(request):
	if request.method == "POST":
		print (request.POST)
		name = request.POST.get('name')
		email = request.POST.get('email')
		query = request.POST.get('query')
		contact1 = Contact(name=name, email=email, query=query, date=datetime.now())
		contact1.save()
	return render(request, 'contact.html')

def recent(request):
    return render(request, 'recent.html')

def create(request):
    return render(request, 'create.html')
 
def appointments(request): 
	
	return render(request, 'appointments.html')

class IndexView(ListView):
	template_name = "myapp/index.html"
	context_object_name = "patient_list"

	def get_queryset(self):
		return Patient.objects.filter(waiting_status=True)


class PatientCreateView(CreateView):
	model = Patient
	fields = "doctor", "patient_name"
	success_url = reverse_lazy("myapp:index")
 

class PatientDetailView(DetailView):
	template_name = "myapp/patient_detail.html"
	model = Patient

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ["patient_name"]
    template_name_suffix = "update_form"
    success_url = reverse_lazy("myapp:index")

class PatientDeleteView(DeleteView):
   model = Patient
success_url = reverse_lazy("myapp:index")

class DoctorDetailView(DetailView):
   template_name = "myapp/doctor_detail.html"
   model = Doctor    	