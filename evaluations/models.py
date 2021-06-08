# Django
from django.db import models

# Models
from students.models import Student


class Rubro(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.student.first_name} - {self.rubro}: {self.score}'
