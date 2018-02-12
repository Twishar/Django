
from django.contrib import admin
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'orders'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    url(r'^orderInfo/$', views.OrderList),

    url(r'^orderInfo/(?P<pk>[0-9]+)/$', views.OrderDetail),

    # /music/album/add/
    url(r'^add/$', views.OrderCreate.as_view(), name='order-add'),

    url(r'admin/', admin.site.urls),

    url(r'orders/(?P<pk>[0-9]+)/delete/$', views.OrderDelete.as_view(), name='order-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)