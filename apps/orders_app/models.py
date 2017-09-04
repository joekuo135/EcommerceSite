from __future__ import unicode_literals

from django.db import models
from ..users_app.models import User
#from ..products_app.models import Product


# Create your models here.
class Order(models.Model):
	user = models.ForeignKey(User, related_name ="users_order", null=True)
	status = models.CharField(max_length=255, null=True) #empty in_process, completed
	#products = models.ManyToManyField(Product)