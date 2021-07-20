# Urls
from django.urls.conf import include

# Forms
from django import forms
from django.forms import fields

# Models
from evaluations.models import Rubro, Evaluation
from students.models import Student


class FormRubro(forms.Form):
    name = forms.CharField(label='Nombre')


class FormRubroCreate(FormRubro):
    name = forms.CharField(label='Nombre')

    def clean_name(self):
        """name field must be unique"""
        name = self.cleaned_data['name']
        name_exists = Rubro.objects.filter(name=name).exists()

        if name_exists:
            raise forms.ValidationError('Ya existe un Rubro con ese nombre')

        return name


class FormRubroDelete(FormRubro):
    name = forms.ModelChoiceField(queryset=Rubro.objects.all())


class FormEvaluation(forms.Form):
    rubro = forms.ModelChoiceField(queryset=Rubro.objects.all())
    score = forms.IntegerField(label='Calificacion', min_value=0, max_value=100)
    student = forms.ModelChoiceField(queryset=Student.objects.all())


class FormEvaluationCreate(FormEvaluation):
    pass


# evaluation form to update
class FormEvaluationUpdate(forms.ModelForm):
    class Meta:
        model = Evaluation

        exclude = ('created', 'updated',)
        # fields = ['score',]
