from django import forms

class CaseForm(forms.Form):
    CONSULTATION_TYPES = [
        ('fi', 'First Visit'),
        ('fo', 'Follow-up'),
        ('su', 'Surgery'),
    ]
    type_of_consultation = forms.ChoiceField(choices=CONSULTATION_TYPES)
    result = forms.CharField(required=False, max_length=1000, widget=forms.Textarea)
    diagnosis = forms.CharField(required=False, max_length=1000, widget=forms.Textarea)
    decision = forms.CharField(required=False, max_length=100)

    def send_hl7(self):
        # TODO: send HL7 message to Mibth using 
        # the self.cleaned_data dictionary
        pass