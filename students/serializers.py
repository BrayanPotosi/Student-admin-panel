from rest_framework import serializers
from .models import (
    Vertical,
    Team,
    Cohort,
    Student,
)


class VerticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vertical
        fields = (
            'id',
            'name'
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'name'
        )


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = (
            'id',
            'name'
        )


class StudentSerializer(serializers.ModelSerializer):
    vertical = TeamSerializer()
    cohort = CohortSerializer()
    team = TeamSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class StudentSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
