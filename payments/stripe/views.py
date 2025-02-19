from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from .utils import create_checkout_session as create_stripe_session  # ✅ Avoid function name conflict

def stripe_checkout(request):
    return render(request, 'stripe_checkout.html', {
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
    })

def stripe_success(request):
    return render(request, 'stripe_success.html')

def stripe_cancel(request):
    return render(request, 'stripe_cancel.html')

@csrf_exempt
def create_checkout_session(request):
    """
    Create a Stripe Checkout Session.
    """
    if request.method != 'POST':  # ✅ Reject GET requests
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        success_url = request.build_absolute_uri('/api/stripe/success/')
        cancel_url = request.build_absolute_uri('/api/stripe/cancel/')
        
        session = create_stripe_session(  # ✅ Call the correct function
            amount=1000,
            currency='usd',
            success_url=success_url,
            cancel_url=cancel_url
        )
        
        return JsonResponse({'sessionId': session['id']})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
