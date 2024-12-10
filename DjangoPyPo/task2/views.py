from django.shortcuts import render
from django.views import View

# Функциональное представление
def function_template(request):
    return render(request, 'second_task/function_template.html')

# Классовое представление
class ClassTemplate(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')
