from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'email_is_verified')
    list_filter = ('is_staff', 'is_active')


admin.site.register(CustomUser, CustomUserAdmin)
