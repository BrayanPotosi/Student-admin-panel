from django.db import models


class Vertical(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.id}, {self.name}'


class Cohort(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.id}, {self.name}'


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.id}, {self.name}'


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    dni = models.CharField(max_length=50, unique=True)
    vertical = models.ForeignKey(Vertical, on_delete=models.SET_NULL, null=True, blank=True)
    cohort = models.ForeignKey(Cohort, null=True, on_delete=models.SET_NULL, blank=True)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.first_name} {self.last_name} {self.dni} {self.vertical}, {self.cohort}, {self.team}, {self.created}'
