from django.contrib import admin
from .models import UserProfile, PPRMapper


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("PPR", "user", "birth_date")
    search_fields = ("PPR", "user__first_name", "user__last_name")

@admin.register(PPRMapper)
class PPRMapperAdmin(admin.ModelAdmin):
    list_display = ("PPR", "employee_name")
    search_fields = ("PPR", "employee_name")