from django.shortcuts import render, redirect
from students.models import Student, Team, Cohort, Vertical
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)
from .serializers import StudentSerializer, TeamSerializer, CohortSerializer, VerticalSerializer, StudentSerializerSimple


# Listar Estudiantes
class StudentsList(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


# Busca un Estudiante por ID
class StudentRetrieveAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.filter()


# Crea un Estudiante
class StudentCreateView(CreateAPIView):
    serializer_class = StudentSerializerSimple


# Borrar Estudiante
class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


# Actualizar Estudiante
class StudentUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentSerializerSimple
    queryset = Student.objects.all()

#===============================#

# Listar Equipos
class TeamsList(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()


# Busca un Equipo por ID
class TeamRetrieveAPIView(RetrieveAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.filter()


# Crea un Equipo
class TeamCreateView(CreateAPIView):
    serializer_class = TeamSerializer


# Borrar Equipo
class TeamDeleteAPIView(DestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


# Actualizar Equipo
class TeamUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

#=============================#

# Listar Cohorts
class CohortList(ListAPIView):
    serializer_class = CohortSerializer

    def get_queryset(self):
        return Cohort.objects.all()


# Busca un Cohort por ID
class CohortRetrieveAPIView(RetrieveAPIView):
    serializer_class = CohortSerializer
    queryset = Cohort.objects.filter()


# Crea un Cohort
class CohortCreateView(CreateAPIView):
    serializer_class = CohortSerializer


# Borrar Cohort
class CohortDeleteAPIView(DestroyAPIView):
    serializer_class = CohortSerializer
    queryset = Cohort.objects.all()


# Actualizar Cohort
class CohortUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CohortSerializer
    queryset = Cohort.objects.all()

#=============================#

# Listar Verticales
class VerticalList(ListAPIView):
    serializer_class = VerticalSerializer

    def get_queryset(self):
        return Vertical.objects.all()


# Busca un Vertical por ID
class VerticalRetrieveAPIView(RetrieveAPIView):
    serializer_class = VerticalSerializer
    queryset = Vertical.objects.filter()


# Crea un Vertical
class VerticalCreateView(CreateAPIView):
    serializer_class = VerticalSerializer


# Borrar Vertical
class VerticalDeleteAPIView(DestroyAPIView):
    serializer_class = VerticalSerializer
    queryset = Vertical.objects.all()


# Actualizar Vertical
class VerticalUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = VerticalSerializer
    queryset = Vertical.objects.all()