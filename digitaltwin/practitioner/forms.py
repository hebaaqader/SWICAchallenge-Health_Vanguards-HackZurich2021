import requests
import logging

from django import forms
from datetime import date

from twin.models import Case

logger = logging.getLogger(__name__)

class CaseForm(forms.Form):
    CONSULTATION_TYPES = [
        ('fi', 'First Visit'),
        ('fo', 'Follow-up'),
        ('su', 'Surgery'),
    ]
    patient_id = forms.IntegerField()
    practitioner_id = forms.IntegerField()
    health_facility_id = forms.IntegerField()
    type_of_consultation = forms.ChoiceField(choices=CONSULTATION_TYPES)
    result = forms.CharField(required=False, max_length=1000, widget=forms.Textarea)
    diagnosis = forms.CharField(required=False, max_length=1000, widget=forms.Textarea)
    decision = forms.CharField(required=False, max_length=100)

    def send_hl7(self):
        # the self.cleaned_data dictionary
        case_id = Case.objects.all().last().pk + 1
        msg = f"""
        MSH|^~\&|HEALTHFACILITYAPP||PATIENTAPP|PATIENT|{date.today()}||ADT^A01||P|2.5
        EVN|A01|{date.today()}
        PID|1|{self.cleaned_data['patient_id']}|||||||||
        PV1|1|O||{self.cleaned_data['type_of_consultation']}|||{self.cleaned_data['practitioner_id']}||||||||||||{case_id}||||||||||||||||||||{self.cleaned_data['health_facility_id']}|||||{date.today()}
        OBX|1|TX|||{self.cleaned_data['result']}|||||F
        DG1|1|||{self.cleaned_data['diagnosis']}|{date.today()}|F
        """
        endpoint = "http://localhost:2021/patient-centricity/"
        try:
            r = requests.post(endpoint, data=str.encode(msg))
            if r.status_code == 201:
                logger.info("Write to Mirth Succeeded!: ")
            else:
                logger.error("Write to Mirth failed with response: " + r.text)
        except requests.exceptions.RequestException as e:
            logger.error("Write to Mirth failed: " + str(e))
