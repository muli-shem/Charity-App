import stripe 
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(amount, currency='usd', success_url=None, cancel_url=None):
      """
    Create a Stripe PaymentIntent.
    :param amount: Amount in cents (e.g., 1000 for $10.00).
    :param currency: Currency code (default: 'usd').
    :return: PaymentIntent object.
    """
      try:
        session= stripe.checkout.Session.create(
           payment_method_types=['card'],
           line_items=[{
               'price_data': {
                   'currency': currency,
                   'product_data': {
                       'name': 'T-shirt',
                   },
                   'unit_amount': amount,
               },
               'quantity': 1,
            }],
            mode ="payment",
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return session
      except Exception as e:
       raise Exception(f"Failed to create Checkout Session: {str(e)}")