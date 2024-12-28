from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
    path('html_sign_up/', views.sign_up_by_html, name='html_sign_up'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.custom_logout, name='logout'),
    path('access-denied/', views.access_denied, name='access_denied'),
]
