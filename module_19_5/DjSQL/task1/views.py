from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Buyer, Game, Cart, News


def shop(request):
    if not request.user.is_authenticated:
        return redirect('login')

    games = Game.objects.all()
    return render(request, 'task1/shop.html', {'games': games})


@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.games.add(game)
    return redirect('shop')


@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'task1/cart.html', {'cart': cart})


@login_required
def remove_from_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cart = Cart.objects.get(user=request.user)
    cart.games.remove(game)
    return redirect('cart')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    buyer = request.user.buyer  # Используем связанный объект Buyer
    total_cost = sum(game.cost for game in cart.games.all())

    if buyer.balance < total_cost:
        return HttpResponse("Недостаточно средств для покупки.")

    for game in cart.games.all():
        if game.age_limited and buyer.age < 18:
            return HttpResponse(f"Возрастное ограничение на игру {game.name}. Покупка невозможна.")

    buyer.balance -= total_cost
    buyer.save()
    cart.games.clear()

    return HttpResponse("Покупка успешно совершена!")


def buy_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    buyer = request.user.buyer

    if game.age_limited and buyer.age < 18:
        return HttpResponse("Возрастное ограничение. Покупка невозможна.")

    return redirect('shop')


def populate_data(request):
    try:
        buyer1, created1 = Buyer.objects.get_or_create(name="Ivan", defaults={"balance": 50, "age": 15})
        buyer2, created2 = Buyer.objects.get_or_create(name="Igor", defaults={"balance": 70.25, "age": 25})
        buyer3, created3 = Buyer.objects.get_or_create(name="Ilya", defaults={"balance": 1500, "age": 30})

        game1, created_game1 = Game.objects.get_or_create(
            name="SILENT HILL 2",
            defaults={"cost": 3500, "size": 5.0, "description": "Silent Hill 2 Remake", "age_limited": False}
        )
        game2, created_game2 = Game.objects.get_or_create(
            name="Until Dawn",
            defaults={"cost": 1000, "size": 4.7, "description": "Interactive drama survival horror",
                      "age_limited": True}
        )
        game3, created_game3 = Game.objects.get_or_create(
            name="Satisfactory",
            defaults={"cost": 2000, "size": 10.0, "description": "First-person open-world factory building game",
                      "age_limited": False}
        )

        game1.buyer.set([buyer1, buyer2, buyer3])
        game2.buyer.set([buyer2, buyer3])
        game3.buyer.set([buyer1, buyer2, buyer3])

        return HttpResponse("Данные успешно добавлены!")
    except Exception as e:
        return HttpResponse(f"Ошибка при добавлении данных: {e}", status=500)


def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)
    return render(request, 'task1/news.html', {'news': news_page})

