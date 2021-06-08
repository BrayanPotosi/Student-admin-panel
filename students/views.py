from django.shortcuts import render, redirect, HttpResponse
from students.models import Student
from students.forms import FormStudent, FormStudentCreate, FormStudentUpdate
from random import randint
# Create your views here.


def list_students(request):
    students_list = Student.objects.all()
    form_student = FormStudent()

    return render(request, template_name='students.html',
                  context={
                      'students_list': students_list,
                      'form': form_student
                  })


def create_student(request):

    if request.method == 'POST':

        student_form = FormStudentCreate(request.POST)

        if student_form.is_valid():
            data_form = student_form.cleaned_data
            first_name = data_form['first_name']
            last_name = data_form['last_name']
            dni = data_form['dni']
            username = f'{first_name[:3]}{last_name[:3]}{randint(1000, 9999)}'
            vertical = request.POST.get('vertical')
            cohort = request.POST.get('cohort')
            team = request.POST.get('team')

            student = Student(
                first_name=first_name,
                last_name=last_name,
                dni=dni,
                username=username,
                vertical_id=vertical,
                cohort_id=cohort,
                team_id=team
            )
            student.save()

            return redirect('students')

        else:
            form = student_form
            students_list = Student.objects.all()
            return render(request=request, template_name='students.html',
                          context={
                              'form': form,
                              'students_list': students_list,
                          })
    else:
        return HttpResponse('Error: Get method is not allowed')


def delete_student(request):

    if request.method == 'POST':
        student_id = request.POST.get('deleteb')
        student = Student.objects.get(pk=student_id)
        student.delete()

    return redirect('students')


def update_student(request):

    if request.method == 'POST':

        student_form = FormStudentUpdate(request.POST)

        if student_form.is_valid():

            data_form = student_form.cleaned_data
            first_name = data_form['first_name']
            last_name = data_form['last_name']
            dni = data_form['dni']
            username = f'{first_name[:3]}{last_name[:3]}{randint(1000, 9999)}'
            vertical = request.POST.get('vertical')
            cohort = request.POST.get('cohort')
            team = request.POST.get('team')

            Student.objects.filter(dni=dni).update(
                first_name=first_name,
                last_name=last_name,
                dni=dni,
                username=username,
                vertical_id=vertical,
                cohort_id=cohort,
                team_id=team
            )

            return redirect('students')

        else:
            return render(request, template_name='update_student.html', context={'update_form': student_form})

    else:
        student_form = FormStudentUpdate()
        return render(request, template_name='update_student.html', context={'update_form': student_form})
