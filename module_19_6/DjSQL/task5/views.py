from django.shortcuts import render, redirect
from task1.models import Buyer, Game, Cart
from .forms import UserRegister
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

def home(request):
    return render(request, 'fifth_task/home.html')

def register(request):
    form = UserRegister(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        repeat_password = form.cleaned_data.get('repeat_password')
        age = form.cleaned_data.get('age')

        if password != repeat_password:
            return render(request, 'fifth_task/registration_page.html', {'form': form, 'error': 'Пароли не совпадают'})
        elif age < 18:
            return render(request, 'fifth_task/registration_page.html', {'form': form, 'error': 'Вы должны быть старше 18'})
        elif Buyer.objects.filter(name=username).exists():
            return render(request, 'fifth_task/registration_page.html', {'form': form, 'error': 'Пользователь уже существует'})
        else:
            user = User.objects.create_user(username=username, password=password)
            Buyer.objects.create(user=user, name=username, balance=0, age=age)
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'fifth_task/registration_page.html', {'form': form, 'success': 'Регистрация прошла успешно'})

    return render(request, 'fifth_task/registration_page.html', {'form': form})

def sign_up_by_django(request):
    form = UserRegister(request.POST or None)
    return register(request)

def sign_up_by_html(request):
    return register(request)

def shop(request):
    games = Game.objects.all()
    return render(request, 'fifth_task/shop.html', {'games': games})

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'fifth_task/cart.html', {'cart': cart})


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def dashboard(request):
    user = request.user
    buyer = Buyer.objects.get(user=user)
    cart = Cart.objects.get(user=user)

    buyers = Buyer.objects.all()
    total_users = buyers.count()
    users_games = {buyer.name: Cart.objects.get(user=buyer.user).games.all() for buyer in buyers}

    context = {
        'buyer': buyer,
        'games': cart.games.all(),
        'total_users': total_users,
        'users_games': users_games,
    }
    return render(request, 'fifth_task/dashboard.html', context)


def access_denied(request):
    return render(request, 'fifth_task/access_denied.html')


def custom_logout(request):
    logout(request)
    return redirect('home')
