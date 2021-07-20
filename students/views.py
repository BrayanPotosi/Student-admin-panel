# Django
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Forms
from students.forms import FormStudent, FormStudentCreate, FormStudentUpdate

# Models
from students.models import Student

from random import randint


@login_required
def list_students(request):
    students_list = Student.objects.all()
    form_student = FormStudent()

    return render(request, template_name='students.html',
                  context={
                      'students_list': students_list,
                      'form': form_student
                  })


@login_required
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
        return HttpResponse('Error: this method is not allowed')


@login_required
def delete_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('deleteb')
        student = Student.objects.get(pk=student_id)
        student.delete()

    return redirect('students')


@login_required
def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    student_form = FormStudentUpdate(request.POST or None, instance=student)

    context = {
        'update_form': student_form,
        'student': student,
    }
    if request.method == 'POST':

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
            return render(request, template_name='update_student.html', context=context)

    else:
        return render(request, template_name='update_student.html', context=context)
