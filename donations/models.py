from django.db import models
from django.contrib.auth.models import User

class Charity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[("Mpesa", "Mpesa"), ("Stripe", "Stripe"), ("PayPal", "PayPal")])
    timestamp = models.DateTimeField(auto_now_add=True)
