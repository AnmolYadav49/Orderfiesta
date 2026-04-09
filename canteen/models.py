from django.db import models
from django.conf import settings

class MenuItem(models.Model):
    CUISINE_CHOICES = (
        ('North Indian', 'North Indian'),
        ('South Indian', 'South Indian'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Beverages', 'Beverages'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    canteen = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 2}) # 2 = IS_CANTEEN
    cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES, default='North Indian')
    customizable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
