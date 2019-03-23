from .models import Request
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db import transaction


class srListView(ListView):
	model = Request
	template_name = 'serviceRequests/SRHomepage.html'
	context_object_name = 'requests'
	ordering = ['-creationDate']
	paginate_by = 10

class srDetailView(DetailView):
	model = Request
	template_name = 'serviceRequests/serviceRequest.html'
	context_object_name = 'request'

class srCreateView(LoginRequiredMixin, CreateView):
	model = Request
	template_name = 'serviceRequests/createRequest.html'
	context_object_name = 'request'
	fields = ['requestType', 'address', 'city', 'state', 'zipCode']
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class srUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Request
	template_name = 'serviceRequests/createRequest.html'
	context_object_name = 'request'
	fields = ['requestType', 'address', 'city', 'state', 'zipCode']
		
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		request = self.get_object()
		if self.request.user == request.user:
			return True
		return False

class srDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Request
	template_name = 'serviceRequests/deleteRequest.html'
	context_object_name = 'request'
	success_url = reverse_lazy('srHome')
	
	def test_func(self):
		request = self.get_object()
		if self.request.user == request.user:
			return True
		return False