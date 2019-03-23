from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'An account has been successfully created for {username}! Please log in.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
		if profile_form.is_valid():
			profile_form.save()
		messages.success(request, f'Your account has been updated!')
		return redirect('profile')
	else:
		profile_form = ProfileUpdateForm(instance = request.user.profile)
	context = {
		'profile_form': profile_form
	}
	return render(request, 'users/profile.html', context)