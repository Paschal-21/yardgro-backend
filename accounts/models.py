from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='farmer')
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    #grocoin_ballance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)   #coded later
    
    def __str__(self):
        return f"{self.username} ({self.role})"