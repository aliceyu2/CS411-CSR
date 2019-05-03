from django.shortcuts import render
from .models import Request
from django.contrib.auth.decorators import login_required
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
from django.db.models import Q
from django.db import connection
import pymysql
pymysql.install_as_MySQLdb()


class srListView(LoginRequiredMixin, ListView):
	model = Request
	template_name = 'serviceRequests/SRHomepage.html'
	context_object_name = 'requests'
	ordering = ['-requestNumber']
	paginate_by = 10

class srDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Request
	template_name = 'serviceRequests/serviceRequest.html'
	context_object_name = 'request'
	
	def test_func(self):
		request = self.get_object()
		if self.request.user == request.user:
			return True
		return False

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

@login_required
def srSearch(request):
	if request.method == 'GET' and 'searchResult' in request.GET:
		query = request.GET['searchResult']
		if query:
			results = []
			cursor = connection.cursor()
			cursor.execute('''DROP PROCEDURE IF EXISTS numOfServiceRequests;''')
			if (query.isdigit()):
				print('number')
				for result in Request.objects.raw("SELECT * FROM serviceRequests_request WHERE requestNumber = '" + query + "' OR zipCode = '" + query + "'"):
					results.append(result)
				cursor.execute("CREATE PROCEDURE numOfServiceRequests() BEGIN SELECT COUNT(*) FROM serviceRequests_request WHERE requestNumber = '" + query + "' OR zipCode = '" + query + "'; END")
			elif (query.isalpha()):
				print('string')
				for result in Request.objects.raw("SELECT * FROM serviceRequests_request WHERE city LIKE '%%" + query + "%%' OR state LIKE '%%" + query + "%%'"):
					results.append(result)
				cursor.execute("CREATE PROCEDURE numOfServiceRequests() BEGIN SELECT COUNT(*) FROM serviceRequests_request WHERE city LIKE '%%" + query + "%%' OR state LIKE '%%" + query + "%%'; END")
			else:
				print('neither')
				for result in Request.objects.raw("SELECT * FROM serviceRequests_request WHERE address LIKE '%%" + query + "%%'"):
					results.append(result)
				cursor.execute("CREATE PROCEDURE numOfServiceRequests() BEGIN SELECT COUNT(*) FROM serviceRequests_request WHERE address LIKE '%%" + query + "%%'; END")
			cursor.callproc('numOfServiceRequests')
			replacement = 'Number of Service Requests: ' + str(cursor.fetchall()[0][0])
			print('replacement: ' + replacement)
			# SHOW PROCEDURE STATUS WHERE name LIKE '%numOfServiceRequests%';
			cursor.close()
			return render(request, 'serviceRequests/SRHomepage.html', {'results': results, 'replacement': replacement})
		else:
			return render(request, 'serviceRequests/SRHomepage.html')
	else:
		return render(request, 'serviceRequests/SRHomepage.html')