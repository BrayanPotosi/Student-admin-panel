from django.shortcuts import render
from django.views.generic import ListView

from .models import Evaluation, Rubro

#Lista todas las evaluaciones en template
class Evaluations(ListView):
    template_name = "evaluations/evaluations.html"
    context_object_name = 'evaluations'

    def get_queryset(self):
        return Evaluation.objects.all()

