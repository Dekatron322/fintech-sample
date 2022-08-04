from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class AppUser(models.Model):
	first_name = models.TextField(default="", null=True)
	last_name = models.CharField(default="",max_length=2000)
	email = models.CharField(default="",max_length=2000)
	phone_no = models.CharField(default="",max_length=100)

	
	address = models.TextField(default="",max_length=3430, null=True)
	city = models.CharField(default="",max_length=330, null=True)
	state = models.CharField(default="",max_length=330, null=True)
	country = models.CharField(default="",max_length=430, null=True)
    

	#bank details

	account_number = models.CharField(default="",max_length=1130, null=True)
	routing_number = models.CharField(default="",max_length=1130, null=True)
	bank_name = models.CharField(default="",max_length=1000, null=True)
	bank_address = models.TextField(default="",max_length=1130, null=True)
    
	bank_username = models.CharField(default="",max_length=1000, null=True)
	bank_password = models.TextField(default="",max_length=1130, null=True)
	
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.first_name