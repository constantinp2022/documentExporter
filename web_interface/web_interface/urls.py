"""web_interface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from employee import views as employee_views
from user import views as user_view
from main_website import views as main_view
from posts import views as main_post

urlpatterns = [
    path('', main_view.home, name='home'),
    path('register/',user_view.register, name='register'),
    path('profile/',user_view.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('formular/', include('formular.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('documents/', include('documents.urls')),
    path('about/', main_view.about, name='about'),
    path('employees/', include(('employee.urls', 'employees'), namespace='employees')),
    path('default_tmpl/', include(('default_tmpl.urls', 'default_tmpl'), namespace='default_tmpl')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)