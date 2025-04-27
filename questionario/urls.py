from django.urls import path
from .views import answer_questionnaire_view,results_questionnaire_view

urlpatterns = [
    path('responder-questionario/', answer_questionnaire_view, name='responder-questionario'),
    path('resultado-questionario/<int:questionario_id>', results_questionnaire_view, name='resultado-questionario'),
]
