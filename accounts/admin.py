from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff') # add 'grocoin_balance' to the tuple later
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')