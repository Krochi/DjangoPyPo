from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'third_task/home.html')

# "Магазин"
def shop(request):
    items = ['Until Dawn', 'Satisfactory', 'SILENT HILL 2']
    context = {'items': items}
    return render(request, 'third_task/shop.html', context)

# "Корзина"
def cart(request):
    return render(request, 'third_task/cart.html')
