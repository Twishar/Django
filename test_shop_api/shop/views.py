from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from shop.serializers import ShopSerializer, DirectorSerializer
from .models import Consultant, Shop, Director
from django.contrib import auth
# Create your views here.


def index(request):
    context = {'username': auth.get_user(request).username}
    return render_to_response('shop/index.html', context)


def shop_view(request):
    shops = Shop.objects.all()
    shop_info = []
    for shop in shops:
        consults = Consultant.objects.filter(shop=shop)
        avg = 0

        for consult in consults:
            avg += consult.sold_goods
        avg = round(avg / 3, 1)

        shop_info.append({'id': shop.id,
                          "title": shop.shop_title,
                          "avg": avg})

    context = {'shop_info': shop_info,
               'username': auth.get_user(request).username}

    return render_to_response('shop/shop_info.html', context)


def director_view(request):
    if auth.get_user(request).is_anonymous:
        return render_to_response('shop/index.html')
    else:
        auth_user = auth.get_user(request)
        print(auth_user)
        director = Director.objects.get(user_id=auth_user)
        shops = Shop.objects.filter(director=director)
        shop_info = []
        for shop in shops:
            consults = Consultant.objects.filter(shop=shop)
            consults_info = []
            for consult in consults:
                consults_info.append({"id": consult.id,
                                      "name": consult.name,
                                      "sold": consult.sold_goods})

            shop_info.append({"id": shop.id,
                              "title": shop.shop_title,
                              "consults_info": consults_info})

        context = {'shop_info': shop_info,
                   'username': auth_user.username}

        return render_to_response('shop/director.html', context)


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
