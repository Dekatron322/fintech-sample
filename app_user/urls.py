from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [

	path("", views.FirstView, name="first"),
	path("second/", views.SecondView, name="second"),
	
]