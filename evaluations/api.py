from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)

from .models import Evaluation, Rubro
from .serializers import EvaluationsSerializer, RubroSerializer, EvaluationsSerializerSimple



#Lista Evaluaciones en JSON
class EvaluationsListAPIView(ListAPIView):
    serializer_class = EvaluationsSerializer

    def get_queryset(self):
        return Evaluation.objects.all()

#Crea una evaluacion
class EvaluationCreateView(CreateAPIView):
    serializer_class = EvaluationsSerializerSimple

#Busca una Evaluacion por ID
class EvaluationRetrieveAPIView(RetrieveAPIView):
    serializer_class = EvaluationsSerializer
    queryset = Evaluation.objects.filter()

#Borrar Evaluacion con ID
class EvaluationDeleteAPIView(DestroyAPIView):
    serializer_class = EvaluationsSerializer
    queryset = Evaluation.objects.all()

#Actualizar Evaluacion
class EvaluationUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = EvaluationsSerializerSimple
    queryset = Evaluation.objects.all()

#========================#
#Lista Rubros en JSON
class RubroListAPIView(ListAPIView):
    serializer_class = RubroSerializer

    def get_queryset(self):
        return Rubro.objects.all()

#Crea un rubro
class RubroCreateView(CreateAPIView):
    serializer_class = RubroSerializer


#Borrar rubro con ID
class RubroDeleteAPIView(DestroyAPIView):
    serializer_class = RubroSerializer
    queryset = Rubro.objects.all()

#Actualizar rubro
class RubroUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = RubroSerializer
    queryset = Rubro.objects.all()