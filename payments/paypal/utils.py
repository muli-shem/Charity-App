import paypalrestsdk
from django.conf import settings

# Set your API credentials, configuration and mode
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # sandbox or live
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

# Create a new credit card
def create_paypal_order(amount, currency ='USD'):
     """
    Create a PayPal order.
    :param amount: Amount to charge (e.g., 10.00 for $10.00).
    :param currency: Currency code (default: 'USD').
    :return: PayPal order object.
    """
     payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "transactions": [
            {
                "amount": {
                    "total": amount,
                    "currency": currency
                }
            }
        ],
        "redirect_urls": {
            "return_url": "http://localhost:8000/api/stripe/success/",
            "cancel_url": "http://localhost:8000/api/stripe/cancel/"
        }
 })
     # Create payment and return the payment object

     if payment.create():
       return payment
     else:
        raise Exception(payment.error)
# Execute a PayPal order
def capture_paypal_order(payment_id):
    """
    Execute a PayPal order.
    :param payment_id: PayPal payment ID.
    :return: PayPal payment object.
    """
    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id":payment.payer.payer_info.payer_id}):
        return payment
    else:
        raise Exception(payment.error)
