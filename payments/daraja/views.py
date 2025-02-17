from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import initiate_stk_push

@csrf_exempt
def initiate_daraja_payment(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            phone_number = data.get('phone_number')
            amount = data.get('amount')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # Check if both fields are provided
        if not phone_number or not amount:
            return JsonResponse({'error': 'Phone number and amount are required'}, status=400)

        try:
            # Call the Daraja STK Push utility function
            response = initiate_stk_push(phone_number, amount)
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)