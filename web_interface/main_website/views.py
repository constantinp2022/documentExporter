from django.shortcuts import render

#Change path to parent directory for aneasier acces to files
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from user.models import Profile
from default_tmpl.models import Default_Templates

def home(request):
	return render(request, 'main_website/home.html')

def about(request):
	return render(request, 'main_website/about.html')