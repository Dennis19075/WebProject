from django.shortcuts import render
from .models import Product, CategoryProd
# Create your views here.
def store(request):
    products = Product.objects.all()
    return render(request, "store/store.html", {'products': products})