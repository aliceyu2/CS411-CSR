from django.conf.urls import url
from django.contrib import admin
from .views import (searchPosts)
from django.urls import path

urlpatterns = [
	url(r'^$', searchPosts, name='searchPosts'),
]