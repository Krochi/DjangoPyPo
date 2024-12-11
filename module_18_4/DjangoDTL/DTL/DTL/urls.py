"""
URL configuration for DTL project.

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
# UrbanDjango/urls.py

from django.contrib import admin
from django.urls import path, include
from task4 import views as task4_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task4_views.home, name='home'),
    path('shop/', task4_views.shop, name='shop'),
    path('cart/', task4_views.cart, name='cart'),
]
