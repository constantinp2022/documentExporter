from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="post-home"),
    path('new', views.new_post, name="post-new"),
]