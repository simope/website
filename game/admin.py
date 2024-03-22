from django.contrib import admin
from .models import Player, Game

# Register your models here.
class Game_admin(admin.ModelAdmin):
    list_display = ["result", "played_at", "player"]

admin.site.register(Game, Game_admin)


class Player_admin(admin.ModelAdmin):
    list_display = ["nickname", "first_visit", "IP", "latitude", "longitude", "points",]

admin.site.register(Player, Player_admin)