from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def url(request, url):
    vendors = [vendor.url for vendor in Shop.objects.all()]
    if url in vendors:
        return render(request, 'home/store.html')
    else:
        return HttpResponse("No vendor found with that name... But don't be sad, use this as an opportunity to make the store yourself!")

def home(request):
    vendors = [vendor for vendor in Shop.objects.all()]
    print(vendors[0].store_name)
    context = {"vendors":vendors}
    return render(request, 'home/home.html', context)

def store(request):
    context = {}
    return render(request, 'home/store.html')

def cart(request):
    context = {}
    return render(request, 'home/cart.html')

def checkout(request):
    context = {}
    return render(request, 'home/checkout.html')