from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .models import Evaluation
from .serializers import EvaluationsSerializer

#Lista todas las evaluaciones en template
class Evaluations(ListView):
    template_name = "evaluations/evaluations.html"
    context_object_name = 'evaluations'

    def get_queryset(self):
        return Evaluation.objects.all()

#Lista Evaluaciones en JSON
class EvaluationsListAPIView(ListAPIView):
    serializer_class = EvaluationsSerializer

    def get_queryset(self):
        return Evaluation.objects.all()

#Crea una evaluacion
class EvaluationCreateView(CreateAPIView):
    serializer_class = EvaluationsSerializer

#Busca una Evaluacion por ID
class EvaluationRetrieveAPIView(RetrieveAPIView):
    serializer_class = EvaluationsSerializer
    queryset = Evaluation.objects.filter()

#Borrar Evaluacion con ID
class EvaluationDeleteAPIView(DestroyAPIView):
    serializer_class = EvaluationsSerializer
    queryset = Evaluation.objects.all()
    
class EvaluationUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = EvaluationsSerializer
    queryset = Evaluation.objects.all()