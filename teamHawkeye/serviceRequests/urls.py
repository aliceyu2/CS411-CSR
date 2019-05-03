from django.urls import path
from .views import (
	srListView,
	srDetailView,
	srCreateView,
	srUpdateView,
	srDeleteView
)
from . import views

urlpatterns  =  [
	path('', srListView.as_view(), name = "srHome"),
	path('<int:pk>/', srDetailView.as_view(), name = 'srDetail'),
	path('new/', srCreateView.as_view(), name = "srCreate"),
	path('<int:pk>/update/', srUpdateView.as_view(), name = 'srUpdate'),
	path('<int:pk>/delete/', srDeleteView.as_view(), name = 'srDelete')
]