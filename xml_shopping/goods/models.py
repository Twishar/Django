from django.db import models

# Create your models here.


class Goods(models.Model):

    article_number = models.IntegerField(unique=True)
    title = models.TextField()
    price = models.IntegerField()
    weight_per_package = models.IntegerField(default=0)
    date_of_creation = models.DateField()
    update_date = models.DateField()
    retail_price = models.IntegerField()
    category = models.TextField()
    color = models.TextField(default='-')
    stock = models.TextField(default='-')



