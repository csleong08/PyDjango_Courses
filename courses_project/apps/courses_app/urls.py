from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^destroy/(?P<course_id>\d+)$', views.show),
    url(r'^destroy/(?P<course_id>\d+)/delete', views.destroy),
]
