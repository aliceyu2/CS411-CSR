from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import (profile)

def searchPosts(request):
	if request.method == 'GET':
		query = request.GET.get('searchResult')
		submitButton = request.GET.get('submit')
		if query is not None:
			lookups = Q(emailAddress__icontains=query) | Q(content__icontains=query)
			results = profile.objects.filter(lookups).distinct()
			print(results)
			context = {'results': results, 'submitButton': submitButton}
			return render(request, 'searchPage.html', context)
		else:
			return render(request, 'searchPage.html')
	else:
		return render(request, 'searchPage.html')