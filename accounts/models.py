from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    IS_ADMIN = 1
    IS_CANTEEN = 2
    IS_USER = 3
    
    ROLE_CHOICES = (
        (IS_ADMIN, 'Admin'),
        (IS_CANTEEN, 'Canteen'),
        (IS_USER, 'User'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=IS_USER)
