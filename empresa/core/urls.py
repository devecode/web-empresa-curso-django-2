from django.urls import path
from . import views



urlpatterns = [

	#Paths core
	path('', views.inicio, name="inicio"),
	path('nosotros/', views.historia, name="historia"),
	path('visitanos/', views.visitanos, name="visitanos"),
]
