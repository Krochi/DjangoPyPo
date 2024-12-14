from django.shortcuts import render
from task1.models import Game

# Главная страница
def home(request):
    return render(request, 'fourth_task/home.html')

# "Магазин"
def shop(request):
    games = Game.objects.all()
    return render(request, 'fourth_task/shop.html', {'games': games})

# "Корзина"
def cart(request):
    return render(request, 'fourth_task/cart.html')
