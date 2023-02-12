from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_tmpl_home, name="home"),
    path('new', views.new_default_tmpl, name="new")
]