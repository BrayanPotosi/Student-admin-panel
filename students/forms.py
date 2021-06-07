from django import forms
from students.models import Vertical, Cohort, Team


class FormStudent(forms.Form):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    dni = forms.IntegerField(label='Identificacion')
    vertical = forms.ModelChoiceField(queryset=Vertical.objects.all())
    cohort = forms.ModelChoiceField(queryset=Cohort.objects.all())
    team = forms.ModelChoiceField(queryset=Team.objects.all())


