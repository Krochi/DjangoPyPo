from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="")
    age_limited = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"