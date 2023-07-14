from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate
from .models import Feedback
from .forms import FeedbackForm
from django_countries import countries
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
# Create your views here.

# @cache_page(600)
def index(request):
    # cache.clear()
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Request successfully sent!!!')
            form.save()
       
           
        # else:
        #     messages.error(request, 'something went wrong')
        #     return redirect('contact')
    else:
        form = FeedbackForm()
        
        
    return render(request, 'test.html', {'form':form})



