from canteen.models import MenuItem
from orders.models import OrderItem
from django.db.models import Count

def get_recommendations(user=None, limit=3):
    popular_items = OrderItem.objects.values('menu_item').annotate(count=Count('menu_item')).order_by('-count')
    if popular_items.exists():
        popular_ids = [item['menu_item'] for item in popular_items[:limit]]
        return MenuItem.objects.filter(id__in=popular_ids)
    return MenuItem.objects.filter(is_available=True)[:limit]

def get_sales_forecast():
    return {
        'today_expected': 120,
        'tomorrow_expected': 145,
        'trend': '+20%',
        'top_category': 'Fast Food'
    }
