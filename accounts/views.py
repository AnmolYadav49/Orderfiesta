from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from canteen.models import MenuItem
from orders.models import Order
from accounts.models import CustomUser
from ai_services.services import get_sales_forecast

@login_required
def admin_dashboard(request):
    if request.user.role != 1:
        return redirect('home')
    users_count = CustomUser.objects.count()
    total_orders = Order.objects.count()
    forecast = get_sales_forecast()
    return render(request, 'admin_dashboard.html', {
        'users_count': users_count, 
        'total_orders': total_orders,
        'forecast': forecast
    })
