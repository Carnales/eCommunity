from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(OrderItem)
admin.site.register(Order)