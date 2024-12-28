# from django.shortcuts import render
# from ..task1.models import Game
#
# def home(request):
#     return render(request, 'fourth_task/home.html')
#
# def shop(request):
#     games = Game.objects.all()
#     return render(request, 'fourth_task/shop.html', {'games': games})
#
# def cart(request):
#     return render(request, 'fourth_task/cart.html')

from django.shortcuts import render
from ..task1.models import Game, Cart
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'fourth_task/home.html')

def shop(request):
    games = Game.objects.all()
    return render(request, 'fourth_task/shop.html', {'games': games})

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'fourth_task/cart.html', {'cart': cart})
