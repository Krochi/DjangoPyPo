# task2/urls.py

from django.urls import path
from .views import function_template, ClassTemplate

urlpatterns = [
    path('function/', function_template, name='function_template'),
    path('class/', ClassTemplate.as_view(), name='class_template'),
]
