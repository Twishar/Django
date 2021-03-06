# Generated by Django 2.1.2 on 2018-11-01 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sold_goods', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_title', models.CharField(max_length=100)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='shop.Director')),
            ],
        ),
        migrations.AddField(
            model_name='consultant',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultants', to='shop.Shop'),
        ),
        migrations.AlterUniqueTogether(
            name='consultant',
            unique_together={('shop', 'name')},
        ),
    ]
