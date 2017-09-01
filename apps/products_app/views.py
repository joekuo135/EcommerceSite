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
		temp = category.split('_') 
		print temp
		category = temp[0]
		subCategory = temp[1]

		all_products = Product.objects.filter(category=category).filter(subCategory=subCategory)
	#print all_products

	content = {
		'products': all_products,
		'categories': ['Mens', 'Womens', 'Kids'],
	}

	return render(request, 'products_app/product_dash.html', content)

def create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price):

	product = Product.objects.create(name=name, category=category, subCategory=subCategory, description=description, fullDescription=fullDescription, image1=image1, image2=image2, image3=image3, image4=image4, size=size, price=price)

	return True

def add_product(request):
	#print postData;
	return render (request, "products_app/addProducts.html")

def process_add_product(request):
	name = ""
	category = ""
	description = ""
	fullDescription = ""
	image1 = "/static/products_app/images/"
	image2 = "/static/products_app/images/"
	image3 = "/static/products_app/images/"
	image4 = "/static/products_app/images/"
	size = ""
	price = ""
	onSale =  "" #(optional) 1: on sale 0: not on sale
	onSale_price = "" #If on sale must set on sale price
	newArrival = "" #(optional) 1 for new, 0 for regular
	
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
def registration(request):
	return redirect('userDashboard/registration.html')

#---------------WOMENS adding item--------------------------
def populate_database(request):
	name = "ROLAND MOURET"
	category = "Womens"
	subCategory = "Apperal"
	description = "Letwell appliqued tulle midi dress"
	fullDescription = " This is a test of fullDescription Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress"
	image1 = "/static/products_app/images/912756_in_xl.jpg"
	image2 = "/static/products_app/images/912756_ou_xl.jpg"
	image3 = "/static/products_app/images/912756_bk_xl.jpg"
	image4 = "/static/products_app/images/912756_detail.mp4"
	size = "Medium"
	price = "3685"
	onSale = 1 #1: on sale 0: not on sale
	onSale_price = 29.99 #If on sale must set on sale price
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	name = "TEMPERLEY LONDON"
	category = "Womens"
	subCategory = "Apperal"
	description = "Starling cold-shoulder embellished chiffon midi dress"
	fullDescription = " This is a test of fullDescription Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress"
	image1 = "/static/products_app/images/913578_in_xl.jpg"
	image2 = "/static/products_app/images/913578_ou_xl.jpg"
	image3 = "/static/products_app/images/913578_bk_xl.jpg"
	image4 = "/static/products_app/images/913578_detail.mp4"
	size = "Medium"
	price = "1200"
	onSale = 1 #1: on sale 0: not on sale
	onSale_price = 29.99 #If on sale must set on sale price
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	name = "ISABEL MARANT"
	category = "Womens"
	subCategory = "Apperal"
	description = "Starling cold-shoulder embellished chiffon midi dress"
	fullDescription = " This is a test of fullDescription Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress"
	image1 = "/static/products_app/images/889614_in_xl.jpg"
	image2 = "/static/products_app/images/889614_ou_xl.jpg"
	image3 = "/static/products_app/images/889614_bk_xl.jpg"
	image4 = "/static/products_app/images/889614_detail.mp4"
	size = "Medium"
	price = "955"
	onSale = 1 #1: on sale 0: not on sale
	onSale_price = 29.99 #If on sale must set on sale price
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
	#---------------MENS adding item--------------------------
	name = "ALEXANDER WANG"
	category = "Womens"
	subCategory = "Footwear"
	description = "Eri studded leather ankle boots"
	image1 = "/static/products_app/images/891293_in_xl.jpg"
	image2 = "/static/products_app/images/891293_fr_xl.jpg"
	image3 = "/static/products_app/images/891293_bk_xl.jpg"
	image4 = "/static/products_app/images/891293_ou_xl.jpg"
	size = "10"
	price = "850"
	onSale = 1 #1: on sale 0: not on sale
	onSale_price = 29.99 #If on sale must set on sale price
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
	#---------------MENS adding item--------------------------
	name = "HERITAGE JACQUARD SUIT"
	category = "Mens"
	subCategory = "Apperal"
	description = "Gucci designer silk jacquard"
	fullDescription = " This is a test of fullDescription Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress"
	image1 = "/static/products_app/images/mens_apparel_001a.jpg"
	image2 = "/static/products_app/images/mens_apparel_001b.jpg"
	image3 = "/static/products_app/images/mens_apparel_001c.jpg"
	size = "46"
	price = 2950
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	name = "WOOLEN SUIT WITH PATCH"
	category = "Mens"
	subCategory = "Apperal"
	description = "Dolce & Gabbana Designer Suit"
	fullDescription = " This is a test of fullDescription Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress"
	image1 = "/static/products_app/images/mens_apparel_002a.jpg"
	image2 = "/static/products_app/images/mens_apparel_002b.jpg"
	image3 = "/static/products_app/images/mens_apparel_002c.jpg"
	image4 = "/static/products_app/images/mens_apparel_002d.jpg"
	size = "44"
	price = 2995
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
	#---------------adding item--------------------------
	name = "SINGLE-BREASTED WEDDING SUIT"
	category = "Mens"
	subCategory = "Apperal"
	description = "Dolce & Gabbana 3-pieces Designer Suit"
	fullDescription = " This is a test of fullDescription Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress Letwell appliqued tulle midi dress"
	image1 = "/static/products_app/images/mens_apparel_003a.jpg"
	image2 = "/static/products_app/images/mens_apparel_003b.jpg"
	image3 = "/static/products_app/images/mens_apparel_003c.jpg"
	image4 = "/static/products_app/images/mens_apparel_003d.jpg"
	size = "48"
	price = 2195
	create_item(request, name, category, subCategory, description, fullDescription, image1, image2, image3, image4, size, price)
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

