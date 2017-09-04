from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
import datetime
from time import gmtime, strftime
import re
import bcrypt
import math
from .models import User
from ..products_app.models import *
from ..orders_app.models import *




# Create your views here.

def index(request):
	print "index"
	return render(request, 'userDashboard/index.html')

def show_map(request):
	print "show_map"
	return render(request, 'userDashboard/map.html')

def registration(request):
	return render(request, 'userDashboard/registration.html')

def login(request):
	return render(request, 'userDashboard/login.html')

# def signin(request):
#     if 'user_id' in request.session:
#         if request.session['isAdmin'] == True:
#             return redirect('/dashboard')
#         return redirect('/products')
#     return render(request, 'userDashboard/login.html')
def user_profile(request):
    user = User.objects.get(id=request.session['id'])
    content ={
    'user': user
    }

    return render(request, 'userDashboard/user_profile.html', content)

def login_user(request):
    print "login_user"
    print "I am in login"
    result = User.objects.login_validator(request.POST)

    if type(result) == dict:
        errors = result
        if len(errors):
            print errors
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/userDashboard/login')

    request.session['id']= result.id
    return redirect('/userDashboard/user_profile')

def create_user(request):
    print "create_user"
    result = User.objects.registration_validator(request.POST)
    print result
    if type(result) == dict:
        errors = result
        if len(errors):
            print errors
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/userDashboard/registration')

    request.session['id']= result.id
    #create cart for users
    Order.objects.create(user=result, status="empty")

    return redirect('/userDashboard/user_profile')


# def user(request, user_id):
#     if 'user_id' not in request.session:
#         messages.error(request, 'You are not logged in.')
#         return redirect('/')

#     owner = User.objects.get(id=user_id)
#     context = {
#         'current_user_id' : request.session['user_id'],
#         'user' : owner,
#     }

#     return render(request, 'userDashboard/user_profile.html', context)

# def dashboard(request):
#     #user must be logged in and must be an admin to see page
#     if request.session.get('user_id', False):
#         user = User.objects.get(id=request.session['user_id'])
#         if user.user_level == 9:
#             context = {
#                'users': User.objects.all()
#             }
#             return render(request, 'userDashboard/dashboard.html', context)
#         else:
#             return redirect('/')
#     else:
#         return redirect('/')

# def create_user(request):

# def admin_create_user(request):

# def user(request, user_id):

# def add_user(request):

# def edit_user(request):

# def edit_user_admin(request, user_id):

# def update_user(request, user_id):

# def delete_user(request, user_id):

# def profile(request, user_id):

# def login(request):

# def logout(request):

# def update_password(request, user_id):

# def prodDashboard(request):

# def prodDashboardsearch(request, searchname, page):