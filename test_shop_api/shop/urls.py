
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('shop_view/', views.shop_view),
    path('director_view/', views.director_view),
]
