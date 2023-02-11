from django.shortcuts import render

#Change path to parent directory for aneasier acces to files
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from statistic.models import Statistic
from main_website.models import Post

def home(request):

	context = {
		'posts':Post.objects.all()
	}
	return render(request, 'main_website/home.html', context)

def about(request):
	return render(request, 'main_website/about.html')