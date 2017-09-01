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

# def signin(request):
#     if 'user_id' in request.session:
#         if request.session['isAdmin'] == True:
#             return redirect('/dashboard')
#         return redirect('/products')
#     return render(request, 'userDashboard/login.html')

# def login(request):
#     if request.method == 'POST':
#         try:
#             current_user = User.objects.get(email = request.POST['email'])
#             if bcrypt.checkpw(request.POST['password'].encode(), current_user.password.encode()):
#                 if request.session['user_id'] == current_user.id()
#                 	request.session['isAdmin'] = True
#                     return redirect('/dashboard')
#                 else:
#                     request.session['isAdmin'] = False
#                     return redirect('/products')
#             else:
#                 messages.error(request, 'Your Login information does not match our database. Please try again.')

#         except:
#             messages.error(request, 'Your Login information does not match our database. Please try again.')
#     return redirect('/signin')

def create_user(request):
    if request.method == 'POST':
        # validate all form data
        errors = User.objects.user_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
            return redirect('/userDashboard/registration')
        else:
            check_email = User.objects.get(email = request.POST['email'])
            messages.error(request, 'Please try another email input.')

            return redirect('/signin')

            hash_it = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                
            # insert user into database
            user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],birthday=request.POST['birthday'],user_level=user_level,password=hash_it)
            user.save()
                
            shoppingCart = ShoppingCart(user=user)
            shoppingCart.save()
            messages.success(request, 'You have successfully registered')
    return redirect('/userDashboard/registration')


def user(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, 'You are not logged in.')
        return redirect('/')

    owner = User.objects.get(id=user_id)
    context = {
        'current_user_id' : request.session['user_id'],
        'user' : owner,
    }

    return render(request, 'userDashboard/user_profile.html', context)

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