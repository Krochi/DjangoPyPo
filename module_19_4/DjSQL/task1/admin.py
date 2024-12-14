from django.contrib import admin
from .models import Game, Buyer

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields_filters = ('size', 'cost')
    fields_display = ('size', 'cost', 'name')
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    fields_filters = ('balance', 'age')
    fields_display = ('balance', 'age', 'name')
    search_fields = ('name',)
    list_per_page = 30
    fields_balance = ('balance',)
