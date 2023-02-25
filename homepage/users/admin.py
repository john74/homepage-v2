from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fields to be used in editing users
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'open_weather_key', 'city')
        }),
    )