import logging

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView

from twin.models import Practitioner, Patient, Case
from twin.utils import *

from practitioner.forms import CaseForm

logger = logging.getLogger(__name__)

def index(request):
    practitioner = Practitioner.objects.filter().first()
    patients = Patient.objects.all()
    context = {'practitioner': practitioner, 'patients': patients}
    return render(request, 'practitioner/index.html', context)

def patient_detail(request, patient_id):
    # TODO: Form the HL7 request and Call Mirth!
    # TODO: parse the incoming json and create a Patient object from it
    # without saving it to database
    patient = get_patient_details(patient_id)
    if not patient:
        logger.error("Error when getting patient data from digital twin, using patient data from local instead")
        patient = Patient.objects.first()
    context = {'patient': patient}
    return render(request, 'practitioner/patient-detail.html', context)

class CaseFormView(FormView):
    template_name = 'practitioner/case-form.html'
    form_class = CaseForm
    success_url = '/practitioner/cases/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_hl7()
        return super().form_valid(form)
