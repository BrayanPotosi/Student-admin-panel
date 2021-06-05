from django.shortcuts import render
from students.models import Student

# Create your views here.


def list_students(request):
    students_list = Student.objects.all()

    return render(request, template_name='students.html', context={'list_students': students_list})
