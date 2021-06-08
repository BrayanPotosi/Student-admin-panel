"""dashboard_upprogram_students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from auth.views import HomeView
from students import views as student_views
from evaluations import views as evaluations_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth.urls', namespace='auth')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', HomeView, name='home'),
    path('students', student_views.list_students, name='students'),
    path('create-student', student_views.create_student, name='create'),
    path('delete-student', student_views.delete_student, name='delete'),
    path('update-student', student_views.update_student, name='update'),
    path('evaluations', evaluations_views.list_evaluation, name='evaluations'),
    path('create-evaluation', evaluations_views.create_evaluation, name='create_evaluation'),
    path('delete-evaluation', evaluations_views.delete_evaluation, name='delete_evaluation'),
    path('update-evaluation', evaluations_views.update_evaluation, name='update_evaluation'),
    path('create-rubro', evaluations_views.create_rubro, name='create_rubro'),
    path('delete-rubro', evaluations_views.delete_rubro, name='delete_rubro' )
]
