from django.shortcuts import render, redirect
from students.models import Student, Cohort, Vertical, Team
import random
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


def create_student(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        dni = request.POST['fdni']
        username = f'{first_name[:3]}{last_name[:3]}{random.randint(100, 9999)}'
        vertical = request.POST['fvertical']
        cohort = request.POST['fcohort']
        team = request.POST['fteam']

        vertical_id = Vertical.objects.get(name__exact=vertical)
        cohort_id = Cohort.objects.get(name__exact=cohort)
        team_id = Team.objects.get(name__exact=team)

        student = Student(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            username= username,
            vertical_id=vertical_id.id,
            cohort_id=cohort_id.id,
            team_id=team_id.id
        )

        student.save()

        return redirect('students')
