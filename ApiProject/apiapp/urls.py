# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.country_list, name='country_list'),
]