from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from orders.views import home, order_list
from canteen.views import dashboard as canteen_dashboard
from accounts.views import admin_dashboard
from ai_services.views import chat_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('orders/', order_list, name='order_list'),
    path('canteen/', canteen_dashboard, name='canteen_dashboard'),
    path('admin-portal/', admin_dashboard, name='admin_dashboard'),
    path('api/chat/', chat_api, name='chat_api'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
