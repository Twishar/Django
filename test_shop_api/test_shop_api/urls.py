from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from shop import views

router = routers.DefaultRouter()
router.register(r'test', views.TestViewSet)
router.register(r'shop', views.ShopwViewSet)
router.register(r'director', views.DirectorViewSet)

urlpatterns = [
    path("shop/", include('shop.urls')),
    url(r'^api_methods/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
