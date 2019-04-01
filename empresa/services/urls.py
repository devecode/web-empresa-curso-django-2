from django.urls import path
from . import views



urlpatterns = [
	#Paths services
	path('', views.servicios, name="servicios"),
]
