from django.contrib import admin

from .models import Student, Cohort, Team, Vertical

admin.site.register(Student)
admin.site.register(Cohort)
admin.site.register(Team)
admin.site.register(Vertical)