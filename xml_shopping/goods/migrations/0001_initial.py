# Generated by Django 2.0.7 on 2018-07-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.IntegerField(unique=True)),
                ('title', models.TextField()),
                ('retail_price', models.IntegerField()),
                ('weight_per_package', models.IntegerField()),
                ('date_of_creation', models.DateField()),
                ('update_date', models.DateField()),
                ('cost_price', models.IntegerField()),
                ('category', models.TextField()),
                ('color', models.TextField()),
                ('stock', models.TextField()),
            ],
        ),
    ]
