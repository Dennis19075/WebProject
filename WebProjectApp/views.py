from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request, "WebProjectApp/home.html")



def store(request):

    return render(request, "WebProjectApp/store.html")



def contact(request):

    return render(request, "WebProjectApp/contact.html")