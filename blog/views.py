from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.template.context_processors import csrf

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())