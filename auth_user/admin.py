from django.contrib import admin
from auth_user.models import UserProfile

@admin.register(UserProfile)
class Profile(admin.ModelAdmin):
    list_display=('phone','iin','user')
    list_filter=('phone','iin','user')
    search_fields = ['user__username']
