
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'goods'

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'upload_files/', views.simple_upload),
    url(r'test_data/', views.test_data),
    url(r'check_data/', views.check_data),
    url(r'reports/', views.reports),
    url(r'report_by_days', views.report_by_days, name='report_by_days'),
    url(r'price_difference_report', views.price_difference_report, name='price_difference_report')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
