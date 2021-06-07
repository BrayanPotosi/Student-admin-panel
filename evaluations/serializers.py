from rest_framework import serializers
from .models import Evaluation, Rubro


class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubro
        fields = (
            'id',
            'name'
        )


class EvaluationsSerializer(serializers.ModelSerializer):
    rubro = RubroSerializer()

    class Meta:
        model = Evaluation
        fields = (
            'id',
            'rubro',
            'score',
            'student',
            'created',
            'updated'
        )
