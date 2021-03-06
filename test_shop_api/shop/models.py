from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=40)
    user_id = models.ForeignKey(User, related_name='director', on_delete=models.CASCADE)


class Shop(models.Model):
    shop_title = models.CharField(max_length=100)
    director = models.ForeignKey(Director, related_name='shops', on_delete=models.CASCADE)


class Consultant(models.Model):
    shop = models.ForeignKey(Shop, related_name='consultants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sold_goods = models.IntegerField()

    class Meta:
        unique_together = ('shop', 'name')
        ordering = ['name']
