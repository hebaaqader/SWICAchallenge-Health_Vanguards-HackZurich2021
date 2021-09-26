from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient-detail'),
    path('patients/<int:patient_id>/cases/new', views.CaseFormView.as_view(), name='new-case'),
    path('cases/thanks/', TemplateView.as_view(template_name="practitioner/thanks.html"))
]   