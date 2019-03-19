from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import createRequest
from django.contrib.auth.decorators import login_required


@login_required
def srHome(request):
	if request.method == 'POST':
		form = createRequest(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('srHome')
	else:
		form = createRequest()
	return render(request, 'serviceRequests/SRHomepage.html', { 'title': 'Service Requests Homepage' , 'form': form})