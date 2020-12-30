from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('cart', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout', views.checkout, name="checkout"),
    path('register/', views.register, name="register"),
    path('register', views.register, name="register"),
    path('log_out/', views.log_out, name="log_out"),
    path('log_out', views.log_out, name="log_out"),
    path('employee/', views.employee, name="employee"),
    path('employee', views.employee, name="employee"),
    path('nchack', views.nchack, name="nchack"),
    path('<url>', views.url, name="url"),
    path('update_item/', views.updateItem, name="update_item")
]