from django.shortcuts import render

# Create your views here.

from django.http  import  HttpResponse

def index(request):
    return HttpResponse("<h1>This should be on azure is the main index.</h1>")

def formular(request):
    return render(request, 'formular/home.html')