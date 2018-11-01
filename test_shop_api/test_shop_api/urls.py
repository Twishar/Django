from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework import routers
from shop import views

router = routers.DefaultRouter()
router.register(r'shop', views.ShopViewSet)
router.register(r'director', views.DirectorViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_methods/', include(router.urls)),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('shop.urls')),
]


