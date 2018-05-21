
from django.contrib import admin
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'noteInfo/', views.NoteList.as_view()),

    url(r'admin/', admin.site.urls),

    # url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # album_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    # /music/album/add/
    url(r'notes/add/$', views.NoteCreate.as_view(), name='note-add'),
    # /music/album/2/
    url(r'notes/(?P<pk>[0-9]+)/$', views.NoteUpdate.as_view(), name='note-update'),
    # /music/album/2/
    url(r'notes/(?P<pk>[0-9]+)/delete/$', views.NoteDelete.as_view(), name='note-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)