
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'goods'

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'simple/', views.simple_upload),
    url(r'test_data/', views.test_data),
    url(r'check_data/', views.check_data),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
