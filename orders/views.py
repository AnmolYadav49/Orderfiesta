from django.shortcuts import render
from canteen.models import MenuItem
from .models import Order
from ai_services.services import get_recommendations

def home(request):
    query = request.GET.get('q', '')
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query, is_available=True) | MenuItem.objects.filter(cuisine__icontains=query, is_available=True)
    else:
        menu_items = MenuItem.objects.filter(is_available=True)
        
    best_sellers = get_recommendations(request.user if request.user.is_authenticated else None, limit=4)
    
    # Group items by cuisine
    grouped_items = {}
    for item in menu_items.distinct():
        if item.cuisine not in grouped_items:
            grouped_items[item.cuisine] = []
        grouped_items[item.cuisine].append(item)
        
    return render(request, 'home.html', {
        'grouped_items': grouped_items, 
        'best_sellers': best_sellers,
        'query': query
    })

def order_list(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {'error': 'Please login.'})
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})
