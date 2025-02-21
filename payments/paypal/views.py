from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .utils import create_paypal_order, capture_paypal_order
from django.shortcuts import render
from django.conf import settings

def paypal_checkout(request):
    return render(request, 'paypal_checkout.html', {
        'PAYPAL_CLIENT_ID': settings.PAYPAL_CLIENT_ID,
    })

@csrf_exempt
def create_paypal_order_view(request):
    if request.method == 'POST':
        try:
            order = create_paypal_order(amount=100)
            print("Created PayPal Order:", order)  # Debugging
            return JsonResponse({'id': order['id']})  # Ensure `id` is used
        except Exception as e:
            print("Error creating order:", e)
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def capture_paypal_order_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            payment_id = data.get('payment_id')

            # Capture the PayPal payment
            payment = capture_paypal_order(payment_id)
            return JsonResponse({'status': 'success', 'payment': payment.to_dict()})
        except Exception as e:
            print("Error capturing order:", e)
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
