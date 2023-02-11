from django.shortcuts import render

# Create your views here.
def documents_home(request):
	context = {
	}
	return render(request, 'documents/home.html', context)