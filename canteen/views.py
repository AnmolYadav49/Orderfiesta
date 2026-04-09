from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MenuItem
from orders.models import Order

@login_required
def dashboard(request):
    if request.user.role != 2:
        return redirect('home')
    menu_items = MenuItem.objects.filter(canteen=request.user)
    total_orders = Order.objects.count()
    return render(request, 'canteen_dashboard.html', {'menu_items': menu_items, 'total_orders': total_orders})
