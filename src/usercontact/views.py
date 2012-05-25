from usercontact.models import UserProfile
from django.contrib.admin.models import User
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render_to_response('index.html', {})

# This method takes info and logs in a user.
def login(request):
    return render_to_response('login.html', {})

# This method takes info, creates a user, and logs in the new user.
def register(request):
    return render_to_response('register.html', {})

# This method shows a user's submitted info, based on if they're logged in or not.
def userinfo(request):
    if request.method == 'POST':
        s=1
    elif request.method == 'GET':
        s=1
    return render_to_response('userinfo.html', {})