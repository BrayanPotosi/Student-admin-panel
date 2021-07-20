from django.urls import path, re_path
from . import api
from students import views as student_views

app_name = 'students'

urlpatterns = [
    path('students', student_views.list_students, name='students'),
    path('create-student', student_views.create_student, name='create'),
    path('delete-student', student_views.delete_student, name='delete'),
    path('api/students/', api.StudentsList.as_view(), name='students_list'),
    path('api/student/create/', api.StudentCreateView.as_view()),
    path('api/student/<pk>/', api.StudentRetrieveAPIView.as_view()),
    path('api/student/delete/<pk>/', api.StudentDeleteAPIView.as_view()),
    path('api/student/update/<pk>/', api.StudentUpdateAPIView.as_view()),
    path('api/teams/', api.TeamsList.as_view()),
    path('api/team/create/', api.TeamCreateView.as_view()),
    path('api/team/<pk>/', api.TeamRetrieveAPIView.as_view()),
    path('api/team/delete/<pk>/', api.TeamDeleteAPIView.as_view()),
    path('api/team/update/<pk>/', api.TeamUpdateAPIView.as_view()),
    path('api/cohorts/', api.CohortList.as_view()),
    path('api/cohort/create/', api.CohortCreateView.as_view()),
    path('api/cohort/<pk>/', api.CohortRetrieveAPIView.as_view()),
    path('api/cohort/delete/<pk>/', api.CohortDeleteAPIView.as_view()),
    path('api/cohort/update/<pk>/', api.CohortUpdateAPIView.as_view()),
    path('api/vertical/', api.VerticalList.as_view()),
    path('api/vertical/create/', api.VerticalCreateView.as_view()),
    path('api/vertical/<pk>/', api.VerticalRetrieveAPIView.as_view()),
    path('api/vertical/delete/<pk>/', api.VerticalDeleteAPIView.as_view()),
    path('api/vertical/update/<pk>/', api.VerticalUpdateAPIView.as_view()),
]
