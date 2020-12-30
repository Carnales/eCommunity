from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

def url(request, url):
    urls = [vendor.url for vendor in Shop.objects.all()]
    vendors = [vendor for vendor in Shop.objects.all()]

    if url in urls:
        vendor = ""
        for v in vendors:
            if v.url == url:
                vendor = v

        matching_products = Product.objects.filter(shop__url=url)

        context = {"products":matching_products, "vendor":vendor}
        return render(request, 'home/store.html', context)
    else:
        return render(request, 'home/no_store.html', {"message":url})

def home(request):
    vendors = [vendor for vendor in Shop.objects.all()]
    print(vendors[0].store_name)

    context = {"vendors":vendors}
    return render(request, 'home/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = 0
    context = {'items':items, 'order':order, 'cartItems':cartItems}

    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                Customer.objects.create(user=user, name=username)

                login(request, user)
                return render(request, "home/registered.html")
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
            return render(request, "home/register.html", {"form":form})
        form = UserCreationForm
        return render(request, "home/register.html", {"form":form})
    return render(request, 'home/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'home/checkout.html')

def updateItem(request):
    data = json.loads(request.body)
    productId = data['product']
    action = data['action']
    print('action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            Customer.objects.create(user=user, name=username)

            login(request, user)
            return render(request, "home/registered.html")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request, "home/register.html", {"form":form})

    form = UserCreationForm
    return render(request, "home/register.html", {"form":form})

def log_out(request):
    logout(request)
    return render(request, "home/logged_out.html")

def employee(request):
    return render(request, "home/employee.html")

def nchack(request):
    return HttpResponse("I luuuuv nowth cawolayna")