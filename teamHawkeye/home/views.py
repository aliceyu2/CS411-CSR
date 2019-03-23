from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def home(request):
	return render(request, 'home/homepage.html', { 'title': 'Homepage' })