from rest_framework import serializers
from .models import Evaluation, Rubro


class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubro
        fields = '__all__'


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

class EvaluationsSerializerSimple(serializers.ModelSerializer):

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