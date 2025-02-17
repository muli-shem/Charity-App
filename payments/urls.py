from django.urls import path, include

urlpatterns = [
    path('daraja/', include('payments.daraja.urls')),
    # path('stripe/', include('payments.stripe.urls')),
    # path('paypal/', include('payments.paypal.urls')),
]