# Generated by Django 2.0 on 2018-02-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='internalID',
            field=models.IntegerField(unique=True),
        ),
    ]