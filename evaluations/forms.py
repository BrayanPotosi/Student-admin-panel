from django import forms
from evaluations.models import Rubro, Evaluation
from students.models import Student


class FormRubro(forms.Form):

    name = forms.CharField(min_length=3, max_length=20)

    def clean_name(self):
        """identification field must be unique"""
        name = self.cleaned_data['name']
        name_exists = Rubro.objects.filter(name=name).exists()

        if name_exists:
            raise forms.ValidationError('Ya existe un Rubro con ese nombre')

        return name


class FormEvaluation(forms.Form):

    rubro = forms.ModelChoiceField(queryset=Rubro.objects.all())
    score = forms.IntegerField(label='Calificacion')
    student = forms.ModelChoiceField(queryset=Student.objects.all())


class FormEvaluationCreate(FormEvaluation):
    pass
