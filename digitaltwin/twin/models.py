from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ssn = models.CharField(max_length=30, verbose_name='SSN')
    birthdate = models.DateField(verbose_name="Birth Date", null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Insurance(models.Model):
    POLICY_TYPES = [
        ('pr', 'Private'),
        ('pu', 'Public'),
    ]
    provider = models.CharField(max_length=100)
    policy_no = models.CharField(max_length=30, verbose_name="Policy Number", blank=True)
    in_type = models.CharField(max_length=100, choices=POLICY_TYPES, verbose_name="Type")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.provider} - {str(self.policy_no)}"

class HealthFacility(models.Model):
    TYPE_CHOICES = [
        ('ho', 'Hospital'),
        ('cl', 'Clinic'),
        ('la', 'Laboratory')
    ]
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    fa_type = models.CharField(max_length=100, verbose_name="Type", choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

class Practitioner(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    SPECIALTY_CHOICES = [
        ("an", "Anaesthesia"),
        ("pa", "Pathology"),
        ("ps", "Psychiatry"),
        ("gp", "General Practitioner"),
        ("pe", "Pediatric"),
        ("de", "Dermatologist"),
        ("ur", "Urologist"),
        ("ne", "Neurologist"),
        ("op", "Opthalmologist")
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=30, blank=True)
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    health_facility = models.ManyToManyField(HealthFacility)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Case(models.Model):
    CONSULTATION_TYPES = [
        ('fi', 'First Visit'),
        ('fo', 'Follow-up'),
        ('su', 'Surgery'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.DO_NOTHING)
    date = models.DateField()
    type_of_consultation = models.CharField(max_length=100, choices=CONSULTATION_TYPES)
    result = models.TextField(blank=True)
    diagnosis = models.TextField(blank=True)
    decision = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{str(self.patient)} - {str(self.practitioner)} - {str(self.date)}"
