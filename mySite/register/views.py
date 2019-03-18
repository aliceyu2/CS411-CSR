from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .forms import registerForm
@csrf_exempt
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = registerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render(request, 'register.html',{"form":form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = registerForm()

    return render(request, 'register.html', {'form': form})