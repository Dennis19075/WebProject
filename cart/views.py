from math import prod
from django.shortcuts import render

# Create your views here.
from .cart import Cart
from store.models import Product
from django.shortcuts import redirect

def addProduct(request, productId):
    cart = Cart(request)
    product = Product.objects.get(id=productId)
    cart.add(product=product)
    return redirect("store")

def deletProduct(request, productId):
    cart = Cart(request)
    product = Product.objects.get(id=productId)
    cart.delete(product=product)
    return redirect("store")

def subtractProduct(request, productId):
    cart = Cart(request)
    product = Product.objects.get(id=productId)
    cart.subtract(product=product)
    return redirect("store")

def clearCart(request, ):
    cart = Cart(request)
    cart.cleanCart()
    return redirect("store")