from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home/home.html')

def store(request):
    context = {}
    return render(request, 'home/store.html')

def cart(request):
    context = {}
    return render(request, 'home/cart.html')

def checkout(request):
    context = {}
    return render(request, 'home/checkout.html')