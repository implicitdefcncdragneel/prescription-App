from django.contrib import admin
from .profile.models import UserProfile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'q1', 'q2', 'q3', 'q4','q5','docfile')
    list_display_links = ('user', 'docfile')
    search_fields = ('user',)




admin.site.register(UserProfile,UserAdmin)
