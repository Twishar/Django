from django.db import models

# Create your models here.


class Goods(models.Model):

    article_number = models.IntegerField(unique=True)
    title = models.TextField()
    retail_price = models.IntegerField()
    weight_per_package = models.IntegerField()
    date_of_creation = models.DateField()
    update_date = models.DateField()
    cost_price = models.IntegerField()
    category = models.TextField()
    color = models.TextField()
    stock = models.TextField()



