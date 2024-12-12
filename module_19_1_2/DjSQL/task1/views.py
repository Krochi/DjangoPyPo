from django.http import HttpResponse
from .models import Buyer, Game

def populate_data(request):
    buyer1, created1 = Buyer.objects.get_or_create(name="Ivan", defaults={"balance": 50, "age": 15})
    buyer2, created2 = Buyer.objects.get_or_create(name="Igor", defaults={"balance": 70.25, "age": 25})
    buyer3, created3 = Buyer.objects.get_or_create(name="Ilya", defaults={"balance": 1500, "age": 30})

    game1, created_game1 = Game.objects.get_or_create(
        name="Game 1",
        defaults={"cost": 35, "size": 5.0, "description": "Game description", "age_limited": False}
    )
    game2, created_game2 = Game.objects.get_or_create(
        name="Game 2",
        defaults={"cost": 100, "size": 1.7, "description": "Game description", "age_limited": True}
    )
    game3, created_game3 = Game.objects.get_or_create(
        name="Game 3",
        defaults={"cost": 20, "size": 2.0, "description": "Game description", "age_limited": False}
    )

    game1.buyer.set([buyer1, buyer2, buyer3])
    game2.buyer.set([buyer2, buyer3])
    game3.buyer.set([buyer1, buyer2, buyer3])

    return HttpResponse("Data populated successfully!")

