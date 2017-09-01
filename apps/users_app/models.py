from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta
import bcrypt
import re


EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
noNumberPls = re.compile(r'^[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}

        if len(postData['email']) <1:
            errors["email1"]= "Please enter your email address!"
            elif not EMAIL_REGEX.match(postData['email']):
                errors["email2"]= "Please enter a valid email address!"

        if len(postData['first_name']) < 1:
            errors["first_name1"] = "First name is required!"
            else:
                if len(postData['first_name']) < 3:
                    errors["first_name2"] = "First name must be at least 3 characters!"
                if not noNumberPls.match(postData['last_name']):
                    errors["first_name3"]= "First name should have no numbers or special characters in it!"

        if len(postData['last_name']) < 1:
            errors["last_name1"] = "Last name is required!"
            else:
                if len(postData['last_name']) < 3:
                    errors["last_name2"] = "Last name must be at least 3 characters!"
                if not noNumberPls.match(postData['last_name']):
                    errors["last_name3"]= "Last name should have no numbers or special characters in it!"

        if len(postData['password']) < 1:
            errors["password1"] = "Password is required!"
            else:
                if len(postData['password']) < 8:
                    errors["password2"] = "Password must be at least 8 characters!"

                if postData['password'] != postData['pass_confirm']:
                    errors["password3"] = "Password and confirmation field must match!"


        if postData['birthday'] == '':
            errors['birthday1'] = "Must enter hired date!"
        else:
            date_format = "%Y-%m-%d"
            input_hired = datetime.strptime(postData['birthday'], date_format)
            now = datetime.now()
            if input_hired >= now:
                errors["birthday2"] = "Date hired can not be in the future!"

        
        return errors


	def login_validator(self, postData):
		errors = {}
		if len(postData['username']) < 1:
			errors["login"] = "Username and password combination not in our record!"
		if len(postData['password']) < 1:
			errors["login"] = "Username and password combination not in our record!"
		try:
			user = User.objects.get(username=postData['username'])
			if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
				errors["login"] = "Password does not match our record."
		except:
			errors["login"] = "Username and password combination are not in our record"
		return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    objects = UserManager()

    
