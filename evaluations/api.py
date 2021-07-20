# Rest Framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)
# Models
from .models import Evaluation, Rubro

# Serializers
from .serializers import EvaluationsSerializer, RubroSerializer, EvaluationsSerializerSimple


# Lista evaluations JSON
class EvaluationsListAPIView(ListAPIView):
    serializer_class = EvaluationsSerializer

    def get_queryset(self):
        return Evaluation.objects.all()


# Create evaluation
class EvaluationCreateView(CreateAPIView):
    serializer_class = EvaluationsSerializerSimple


# Search evaluation by id
class EvaluationRetrieveAPIView(RetrieveAPIView):
    serializer_class = EvaluationsSerializer
    queryset = Evaluation.objects.filter()


# Delete evaluation by ID
class EvaluationDeleteAPIView(DestroyAPIView):
    serializer_class = EvaluationsSerializer
    queryset = Evaluation.objects.all()


# Update evaluation
class EvaluationUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = EvaluationsSerializerSimple
    queryset = Evaluation.objects.all()


# ========================#
# List Rubros en JSON
class RubroListAPIView(ListAPIView):
    serializer_class = RubroSerializer

    def get_queryset(self):
        return Rubro.objects.all()


# Create rubro
class RubroCreateView(CreateAPIView):
    serializer_class = RubroSerializer


# Delete rubro by ID
class RubroDeleteAPIView(DestroyAPIView):
    serializer_class = RubroSerializer
    queryset = Rubro.objects.all()


# Update rubro
class RubroUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = RubroSerializer
    queryset = Rubro.objects.all()
