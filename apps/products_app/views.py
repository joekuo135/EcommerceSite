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
import math, random
from models import Product




# Create your views here.

def index(request):
	print "products_app index"
	#get featured products
	products = Product.objects.all()
	featuredProducts = []
	ids = []
	for product in products:
		ids.append(product.id)

	#print temp
	for i in range(0,6):
		randomProduct_id = ids[random.randint(0, len(ids)-1)]
		temp = Product.objects.get(id =randomProduct_id)
		featuredProducts.append(temp)

	print featuredProducts

	context = { 'featuredProducts': featuredProducts, }

	return render(request, 'userDashboard/index.html', context)

def show(request):

	return render(request, 'products_app/show.html')

def show_product(request, product_id):
	print "show product"
	product = Product.objects.get(id=product_id)
	print product
	return render(request, 'products_app/product_profile.html', {'product': product})

def show_dashboard(request, category="all"):
	print "show dashboard"
	if category=="all":
		all_products = Product.objects.all()
	else:
		all_products = Product.objects.filter(category=category)
	#print all_products

	content = {
		'products': all_products,
		'categories': ['Mens', 'Womens', 'Kids'],
	}

	return render(request, 'products_app/product_dash.html', content)

def create_item(request, name, category,description, image1, image2, image3, image4, size, price):

	product = Product.objects.create(name=name, category=category, description=description, image1=image1, image2=image2, image3=image3, image4=image4, size=size, price=price)

	return True

def populate_database(request):
	name = "ROLAND MOURET"
	category = "Womens"
	description = "Letwell appliqued tulle midi dress"
	image1 = "/static/products_app/images/912756_in_xl.jpg"
	image2 = "/static/products_app/images/912756_ou_xl.jpg"
	image3 = "/static/products_app/images/912756_bk_xl.jpg"
	image4 = "/static/products_app/images/912756_detail.mp4"
	size = "Medium"
	price = "$3,685"
	onSale = 1 #1: on sale 0: not on sale
	onSale_price = 29.99 #If on sale must set on sale price
	create_item(request, name, category,description, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	name = "TEMPERLEY LONDON "
	category = "Womens"
	description = "Starling cold-shoulder embellished chiffon midi dress"
	image1 = "/static/products_app/images/913578_in_xl.jpg"
	image2 = "/static/products_app/images/913578_ou_xl.jpg"
	image3 = "/static/products_app/images/913578_bk_xl.jpg"
	image4 = "/static/products_app/images/913578_detail.mp4"
	size = "Medium"
	price = "$1,200"
	onSale = 1 #1: on sale 0: not on sale
	onSale_price = 29.99 #If on sale must set on sale price
	create_item(request, name, category,description, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	name = "TEMPERLEY LONDON "
	category = "Womens"
	description = "Starling cold-shoulder embellished chiffon midi dress"
	image1 = "/static/products_app/images/889614_in_xl.jpg"
	image2 = "/static/products_app/images/889614_ou_xl.jpg"
	image3 = "/static/products_app/images/889614_bk_xl.jpg"
	image4 = "/static/products_app/images/889614_detail.mp4"
	size = "Medium"
	price = "$955"
	onSale = 1 #1: on sale 0: not on sale
	onSale_price = 29.99 #If on sale must set on sale price
	create_item(request, name, category,description, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	name = "Timerland Hiking Boot"
	category = "Mens"
	description = "Men's Limited Release 1978 Waterproof Hiking Boots"
	image1 = "/static/products_app/images/boot1.png"
	image2 = "/static/products_app/images/boot2.png"
	image3 = "/static/products_app/images/boot3.png"
	image4 = "/static/products_app/images/boot4.png"
	size = "9"
	price = 250
	create_item(request, name, category,description, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	# name = ""
	# category = ""
	# description = ""
	# image1 = "/static/products_app/images/"
	# image2 = "/static/products_app/images/"
	# image3 = "/static/products_app/images/"
	# image4 = "/static/products_app/images/"
	# size = ""
	# price = 
	# onSale =  #(optional) 1: on sale 0: not on sale
	# onSale_price = #If on sale must set on sale price
	# newArrival = #(optional) 1 for new, 0 for regular
	#
	# create_item(request, name, category,description, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	


	all_products = Product.objects.all()
	#print all_products

	content = {
		'products': all_products
	}

	return render(request, 'products_app/show.html', content)

