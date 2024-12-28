from django.contrib import admin
from .models import Game, Buyer, News

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')
    list_display = ('size', 'cost', 'name')
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')
    list_display = ('balance', 'age', 'name')
    search_fields = ('name',)
    list_per_page = 30


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')
    list_per_page = 15

