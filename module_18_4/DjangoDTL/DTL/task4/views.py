from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'fourth_task/home.html')

# "Магазин"
def shop(request):
    games = ['Until Dawn', 'Satisfactory', 'SILENT HILL 2']
    context = {'games': games}
    return render(request, 'fourth_task/shop.html', context)

# "Корзина"
def cart(request):
    return render(request, 'fourth_task/cart.html')
