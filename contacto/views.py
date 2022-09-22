from ast import If
from django.shortcuts import render, redirect

from .forms import ContactForm

from django.core.mail  import EmailMessage

# Create your views here.
def contacto(request):
    form = ContactForm()

    if(request.method=="POST"):
        form=ContactForm(data=request.POST)
        if(form.is_valid()):
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            emailMes = EmailMessage(
                "Message from App Django",
                "The user {} with email {} wrote this message for you:\n\n {} ".format(name,email,content), "", ["dennis.chicaiza.a@gmail.com"], reply_to=[email])
            try:
                emailMes.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {'form': form})