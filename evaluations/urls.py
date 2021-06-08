from django.urls import path, re_path
from . import views

app_name = 'evaluations'

urlpatterns = [
    path('evaluations/', views.Evaluations.as_view(), name='evaluations'),
    path('api/evaluations/', views.EvaluationsListAPIView.as_view()),
    path('api/evaluation/create/', views.EvaluationCreateView.as_view()),
    path('api/evaluation/<pk>/', views.EvaluationRetrieveAPIView.as_view()),
    path('api/evaluation/delete/<pk>/', views.EvaluationDeleteAPIView.as_view()),
    path('api/evaluation/update/<pk>/', views.EvaluationUpdateAPIView.as_view()),
    path('api/rubros/', views.RubroListAPIView.as_view()),
    path('api/rubro/create/', views.RubroCreateView.as_view()),
    path('api/rubro/delete/<pk>/', views.RubroDeleteAPIView.as_view()),
    path('api/rubro/update/<pk>/', views.RubroUpdateAPIView.as_view()),
]
