from django import forms
from students.models import Student, Vertical, Cohort, Team


class FormStudent(forms.Form):

    first_name = forms.CharField(label='Nombre', min_length=3, max_length=20, )
    last_name = forms.CharField(label='Apellido', min_length=3, max_length=20)
    dni = forms.IntegerField(label='Identificacion',min_value=1000, max_value=9999999999)
    vertical = forms.ModelChoiceField(queryset=Vertical.objects.all())
    cohort = forms.ModelChoiceField(queryset=Cohort.objects.all())
    team = forms.ModelChoiceField(queryset=Team.objects.all())


class FormStudentCreate(FormStudent):

    def clean_dni(self):
        """identification field must be unique"""
        dni = self.cleaned_data['dni']
        dni_exists = Student.objects.filter(dni=dni).exists()

        if dni_exists:
            raise forms.ValidationError('Ya existe un usuario con esa identificacion registrado')

        return dni


class FormStudentUpdate(FormStudent):

    def clean_dni(self):
        """identification field must be exist"""
        dni = self.cleaned_data['dni']
        dni_exists = Student.objects.filter(dni=dni).exists()

        if not dni_exists:
            raise forms.ValidationError('No existe un usuario con esa identificacion')

        return dni


