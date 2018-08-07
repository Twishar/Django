from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from mptt_client import admin

urlpatterns = (
    # Examples:
    # url(r'^$', 'mptthowto.views.home', name='home'),
    url(r'^main/', include('mptt_client.urls')),
)
