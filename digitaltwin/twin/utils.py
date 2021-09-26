import requests, logging

from twin.models import Patient, Case, Practitioner, HealthFacility

logger = logging.getLogger(__name__)

def get_patient_details(patient_id):
    endpoint = f"http://localhost:2020/patient-centricity?patientId={patient_id}"
    try:
        r = requests.get(endpoint)
    except requests.exceptions.RequestException as e:
        logger.error("Request to Mirth failed: " + str(e))
        return
    if r.status_code == requests.codes.ok:
        try:
            res_json = r.json()
        except requests.exceptions.InvalidJSONError:
            logger.error("Mirth response is not a valid JSON " + str(e))
            return
     

        patient = Patient(
            id=res_json['patient_id'],
            first_name=res_json['patient_first_name'],
            last_name=res_json['patient_last_name'],
            birthdate=res_json['patient_birthdate'],
            gender=res_json['patient_gender']
            )
        for case in res_json['cases']:
            c = Case(
                practitioner=Practitioner.objects.get(pk=case['practitioner_id']),
                health_facility=HealthFacility.objects.get(pk=case['health_facility_id']),
                date=case['date'],
                type_of_consultation=case['type_of_consultation'],
                result=case['result'],
                diagnosis=case['diagnosis'],
                decision=case['decision']
                )
            patient.case_set.add(c, bulk=False)
        return patient