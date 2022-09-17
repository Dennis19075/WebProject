from django.shortcuts import render

# Create your views here.
from servicios.models import Servicio

def services(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/services.html", {"servicios": servicios})