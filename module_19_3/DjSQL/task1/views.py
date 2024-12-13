from django.http import HttpResponse
from .models import Buyer, Game

def populate_data(request):
    try:

        buyer1, created1 = Buyer.objects.get_or_create(name="Ivan", defaults={"balance": 50, "age": 15})
        buyer2, created2 = Buyer.objects.get_or_create(name="Igor", defaults={"balance": 70.25, "age": 25})
        buyer3, created3 = Buyer.objects.get_or_create(name="Ilya", defaults={"balance": 1500, "age": 30})

        print(f"Покупатели: {buyer1}, {buyer2}, {buyer3}")

        game1, created_game1 = Game.objects.get_or_create(
            name="SILENT HILL 2",
            defaults={"cost": 3500, "size": 5.0, "description": "Silent Hill 2 Remake", "age_limited": False}
        )
        game2, created_game2 = Game.objects.get_or_create(
            name="Until Dawn",
            defaults={"cost": 1000, "size": 4.7, "description": "Interactive drama survival horror", "age_limited": True}
        )
        game3, created_game3 = Game.objects.get_or_create(
            name="Satisfactory",
            defaults={"cost": 2000, "size": 10.0, "description": "First-person open-world factory building game", "age_limited": False}
        )

        print(f"Игры: {game1}, {game2}, {game3}")

        game1.buyer.set([buyer1, buyer2, buyer3])
        game2.buyer.set([buyer2, buyer3])
        game3.buyer.set([buyer1, buyer2, buyer3])

        print(f"Связь установлена: {game1.buyer.all()}, {game2.buyer.all()}, {game3.buyer.all()}")

        return HttpResponse("Данные успешно добавлены!")
    except Exception as e:
        print(f"Ошибка при добавлении данных: {e}")
        return HttpResponse("Произошла ошибка при добавлении данных.", status=500)
