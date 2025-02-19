from django.urls import path
from .views import create_checkout_session, stripe_checkout, stripe_success, stripe_cancel

urlpatterns = [
    path('checkout/', stripe_checkout, name='stripe-checkout'),
    path('success/', stripe_success, name='stripe-success'),
    path('cancel/', stripe_cancel, name='stripe-cancel'),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
]
