from django.conf.urls import  include, url

from mptt_client.views import show_genres

urlpatterns = (
    url(r'^genres/$', show_genres),
)

