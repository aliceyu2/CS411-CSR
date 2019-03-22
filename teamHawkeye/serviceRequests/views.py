from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import createRequest
from django.contrib.auth.decorators import login_required
from .models import Request
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


@login_required
def srHome(request):
	context = {
		'requests': Request.objects.all()
	}
	return render(request, 'serviceRequests/SRHomepage.html', context, { 'title': 'Service Requests Homepage' })

class srListView(ListView):
	model = Request
	template_name = 'serviceRequests/SRHomepage.html'
	context_object_name = 'requests'
	ordering = ['-priority']
	paginate_by = 10

class srDetailView(DetailView):
	model = Request
	template_name = 'serviceRequests/serviceRequest.html'
	context_object_name = 'request'
	paginate_by = 10

@login_required
def srCreate(request):
	if request.method == 'POST':
		form = createRequest(request.POST)
		if form.is_valid():
			currentRequest = form.save(commit = False)
			currentRequest.user = request.user
			currentRequest.save()
			messages.success(request, f'Your request has been created!')
			return redirect('srHome')
	else:
		form = createRequest()
	return render(request, 'serviceRequests/SRCreate.html', { 'title': 'Create a Service Request' , 'form': form})