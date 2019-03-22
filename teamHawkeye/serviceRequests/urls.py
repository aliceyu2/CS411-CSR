from django.urls import path
from .views import (
	srListView,
	srDetailView
)
from . import views

urlpatterns  =  [
	path('', views.srListView.as_view(), name = "srHome"),
	path('serviceRequest/<int:pk>/', views.srDetailView.as_view(), name = 'srDetail'),
	path('create/', views.srCreate, name = "srCreate"),
]