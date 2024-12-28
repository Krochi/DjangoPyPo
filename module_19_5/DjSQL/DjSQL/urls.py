"""
URL configuration for DjSQL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from task1 import views as task1_views
from task5 import views as task5_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task5.urls')),
    path('task1/', include('task1.urls')),
    #path('task4/', include('task4.urls')), #только что добавил
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='accounts_login'),
    path('news/', task1_views.news, name='news'),
    path('dashboard/', task5_views.dashboard, name='dashboard'),
    path('platform/register/', task5_views.register, name='register'),
    path('shop/', task5_views.shop, name='shop'),
    path('cart/', task1_views.cart, name='cart'),
    path('add_to_cart/<int:game_id>/', task1_views.add_to_cart, name='add_to_cart'),
]
