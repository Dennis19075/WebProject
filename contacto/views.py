from django.shortcuts import render

from .forms import ContactForm

# Create your views here.
def contacto(request):
    form = ContactForm()

    return render(request, "contacto/contacto.html", {'form': form})