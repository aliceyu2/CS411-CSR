from django.conf.urls import url
from django.contrib import admin
from .views import (goToHomepage)
from django.urls import path

urlpatterns = [
	url(r'^$', goToHomepage, name='goToHomepage'),
]