from django.shortcuts import render
from students.models import Student

# Create your views here.


def get_students(request):
    list_students = Student.objects.get(id=1)
    return render(request, template_name='students.html')
