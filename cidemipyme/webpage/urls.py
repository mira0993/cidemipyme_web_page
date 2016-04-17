from django.conf.urls import url
from . import views

__author__ = 'ines'


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
