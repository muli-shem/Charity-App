from django.urls import path
from . import views

urlpatterns = [
    path('create-order/', views.create_paypal_order_view, name='create_paypal_order'),
    path('capture-order/', views.capture_paypal_order_view, name='capture_paypal_order'),
    path('checkout/', views.paypal_checkout, name='paypal_checkout'),
]