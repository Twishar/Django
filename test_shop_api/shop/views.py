from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from shop.serializers import TestSerializer, ShopSerializer, DirectorSerializer
from .models import Test, Consultant, Shop, Director
# Create your views here.


def index(request):
    shop = Shop.objects.get(shop_number="Shop #1")
    consults = Consultant.objects.filter(shop=shop)
    avg = 0

    for consult in consults:
        avg += consult.sold_goods
        print(consult.shop.shop_number)
    avg = avg/3
    context = {'data': avg}
    return render(request, 'shop/index.html', context)


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class ShopwViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
