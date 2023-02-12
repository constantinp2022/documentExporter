from django.shortcuts import render, redirect
from .models import Post
from .forms import NewPostForm
from django.contrib import messages

# Create your views here.
def posts(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'user_post.html', context)

def new_post(request):
	if request.method == 'POST':
		new_post_form = NewPostForm(request.POST)
		if  new_post_form.is_valid():
			new_post_form.save()
			messages.success(request, f'Message stored!')
			return redirect('posts:post-home')

	else:
		new_post_form = NewPostForm()

	context = {
		'new_post_form' : new_post_form
	}

	return render(request, 'new_post.html', context)