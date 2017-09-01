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
from models import User
from ..products_app.models import Product
from ..orders_app.models import Order




# Create your views here.

def index(request):
	print "index"
	return render(request, 'orders_app/cart.html')



def update_cart(request, product_id):
	#get product
	product = Product.objects.get(id=product_id)
	#get users order
	order = Order.objects.get(user=request.session['id'])
	order.objects.add.products(product)
	return render(request, '/carts')


	

