# Generated by Django 2.0.7 on 2018-07-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='cost_price',
        ),
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
