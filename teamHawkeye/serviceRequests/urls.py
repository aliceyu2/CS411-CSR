from django.urls import path
from . import views

urlpatterns  =  [
	path('', views.srHome, name = "srHome"),
	path('create/', views.srCreate, name = "srCreate"),
]