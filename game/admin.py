from django.contrib import admin
from .models import rps_match, user

# Register your models here.
class rps_match_admin(admin.ModelAdmin):
    list_display = ["result", "created_at",]

admin.site.register(rps_match, rps_match_admin)


class user_admin(admin.ModelAdmin):
    list_display = ["ip", "latitude", "longitude", "points", "created_at",]

admin.site.register(user, user_admin)