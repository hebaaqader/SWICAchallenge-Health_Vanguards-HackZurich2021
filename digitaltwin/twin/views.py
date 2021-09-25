from django.shortcuts import render
from django.http import HttpResponse

from .models import Patient

def index(request):
    client = Patient.objects.filter().first()
    context = {'client': client}
    return render(request, 'twin/index.html', context)