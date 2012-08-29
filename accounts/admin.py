from django.contrib import admin
from models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday')

admin.site.register(Profile, ProfileAdmin)