from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
@login_required
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '').lower()
            
            if 'pizza' in message:
                reply = "We highly recommend the Spicy Pepperoni Pizza! Should I add it to your cart?"
            elif 'recommend' in message or 'suggest' in message:
                reply = "Based on current trends, the Grilled Chicken Sandwich is very popular today!"
            else:
                reply = "I'm your Orderista AI assistant. I can help you find food or make recommendations. What are you craving?"
                
            return JsonResponse({'reply': reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method.'}, status=405)
