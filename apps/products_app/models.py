from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=255) 
	category = models.CharField(max_length=255) #Mens, Womens, Kids,
	description = models.TextField()
	image1 = models.CharField(max_length=255)
	image2 = models.CharField(max_length=255)
	image3 = models.CharField(max_length=255)
	image4 = models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	price = models.FloatField()
	onSale = models.BooleanField(default = 0) 
	onSale_price = models.FloatField(null=True)
	newArrival = models.BooleanField(default = 0)
	

	
	
	
