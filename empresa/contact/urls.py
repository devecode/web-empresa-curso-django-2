from django.urls import path
from . import views

urlpatterns = [
	#Paths contacto
	path('', views.contact, name="contact"),
]
