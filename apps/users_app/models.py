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
        #create object to store errors
        error ={}
        #validate email
        print "this is email", postData['email']
        if len(User.objects.filter(email=postData['email'])) > 0:
            print "result", User.objects.filter(email=postData['email'])
            error['email'] = "User already registered, please login"
            return error
        #validate name
        if len(postData['first_name']) < 3:
            error['first_name'] = "first name should be more than 2 characters"
            #validate name
        if len(postData['last_name']) < 3:
            error['last_name'] = "last name should be more than 2 characters"
        #validate email
        if len(postData['email']) < 3:
            error['email'] = "email should be more than 2 characters"
        #validate password
        if len(postData['password']) < 6:
            error['password'] = "Password must be at least 8 characters"
        #password confirmation does not match
        if postData['password'] != postData['conf_pass']:
            error['password'] = "Passwords do not match"

        try:
            today = date.time.now()
            if datetime.strptime(postData['birthday'], '%Y-%m-%d') > today.date():
                error['birthday'] = "birthday date cannot be in the future"
        except:
            if postData['birthday'] == "":
                error["birthday"] = "birthday date cannot be empty"
        if error:
            return error

        #If passes all validations create user
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        birthday = postData['birthday']
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, birthday=birthday)

        return user

    def login_validator(self, postData):
        error = {}
        if postData['email'] == "":
            error['email'] = "email cannot be empty"
        if postData['password'] == "":
            error['password'] = "Password cannot be empty"
        
        if error:
            return error

        #check if user is the database
        if len(User.objects.filter(email=postData['email'])) > 0:
            user = User.objects.filter(email=postData['email'])[0]
            #compare passwords
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                error['password'] = 'Incorrect password'
        else:
            error['password'] = 'Please register'

        if error:
            return error
        return user

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    objects = UserManager()

    
