from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Test, Shop, Consultant, Director


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('title', 'description')


class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ('name', 'sold_goods')


class ShopSerializer(serializers.ModelSerializer):
    consultants = ConsultantSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('shop_title', 'consultants')


class DirectorSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ('name', 'shops')
