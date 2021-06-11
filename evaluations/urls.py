from django.urls import path, re_path
from . import api, views

app_name = 'evaluations'

urlpatterns = [
    path('evaluations/', views.Evaluations.as_view(), name='evaluations'),
    path('api/evaluations/', api.EvaluationsListAPIView.as_view()),
    path('api/evaluation/create/', api.EvaluationCreateView.as_view()),
    path('api/evaluation/<pk>/', api.EvaluationRetrieveAPIView.as_view()),
    path('api/evaluation/delete/<pk>/', api.EvaluationDeleteAPIView.as_view()),
    path('api/evaluation/update/<pk>/', api.EvaluationUpdateAPIView.as_view()),
    path('api/rubros/', api.RubroListAPIView.as_view()),
    path('api/rubro/create/', api.RubroCreateView.as_view()),
    path('api/rubro/delete/<pk>/', api.RubroDeleteAPIView.as_view()),
    path('api/rubro/update/<pk>/', api.RubroUpdateAPIView.as_view()),
]
