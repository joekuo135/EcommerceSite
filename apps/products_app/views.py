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
from models import Product




# Create your views here.

def index(request):
	return render(request, 'userDashboard/index.html')

def show(request):

	return render(request, 'products_app/show.html')

def create_item(request):
	name = "Timerland Hiking Boot"
	category = "Mens"
	description = "Men's Limited Release 1978 Waterproof Hiking Boots"
	image1 = "/static/products_app/images/boot1.png"
	image2 = "/static/products_app/images/boot2.png"
	image3 = "/static/products_app/images/boot3.png"
	image4 = "/static/products_app/images/boot4.png"
	size = "9"
	price = "250"

	product = Product.objects.create(name=name, category=category, description=description, image1=image1, image2=image2, image3=image3, image4=image4, size=size, price=price)

	all_products = Product.objects.all()
	print all_products

	content = {
		'products': all_products
	}

	return render(request, 'products_app/show.html', content)

def show_dashboard(request):

	all_products = Product.objects.all()
	print all_products

	content = {
		'products': all_products
	}

	return render(request, 'userDashboard/index.html', content)
