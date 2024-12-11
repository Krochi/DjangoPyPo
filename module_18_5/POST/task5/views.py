from django.shortcuts import render, redirect
from .forms import UserRegister

users = ['user1', 'user2', 'user3']

def get_registration(request, form=None, is_django_form=False):
    info = {}
    if request.method == 'POST':
        if is_django_form and form:
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                repeat_password = form.cleaned_data.get('repeat_password')
                age = form.cleaned_data.get('age')
            else:
                info['error'] = 'Некорректные данные формы'
                info['form'] = form
                return render(request, 'fifth_task/registration_page.html', info)
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if age:
                try:
                    age = int(age)
                except ValueError:
                    info['error'] = 'Неверное значение возраста'
                    return render(request, 'fifth_task/registration_page.html', info)
            else:
                info['error'] = 'Возраст не указан'
                return render(request, 'fifth_task/registration_page.html', info)

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f'Приветствуем, {username}!'
            users.append(username)
            #return redirect('home')

    info['form'] = form if is_django_form else UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_django(request):
    form = UserRegister(request.POST or None)
    return get_registration(request, form, is_django_form=True)

def sign_up_by_html(request):
    return get_registration(request)

