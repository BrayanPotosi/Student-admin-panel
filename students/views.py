from django.shortcuts import render
from students.models import Student, Cohort, Vertical, Team

# Create your views here.


def list_students(request):
    students_list = Student.objects.all()
    vertical_list = Vertical.objects.all()
    cohorts_list = Cohort.objects.all()
    team_list = Team.objects.all()

    return render(request, template_name='students.html',
                  context={
                      'students_list': students_list,
                      'vertical_list': vertical_list,
                      'cohorts_list': cohorts_list,
                      'team_list': team_list
                  })