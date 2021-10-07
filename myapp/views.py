from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	context = {
	'variable1': "hey pathavla aahey re",
	'variable2': "baghun ghey re baba"

	}
	return render(request, 'index.html', context)
	#return HttpResponse("This is my starting page")

	
def about(request):
	return HttpResponse("My about page")


def info(request):
	return HttpResponse("information of my app page")


def contact(request):
    return render(request, 'contact.html')


def recent(request):
    return render(request, 'recent.html')


def create(request):
    return render(request, 'create.html')

 
def workspace(request):
	return render(request, 'workspace.html')
	#return HttpResponse("This is my starting page")