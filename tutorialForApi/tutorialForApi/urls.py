
from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from companies import views
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'stocks/', views.StockList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

