from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('services/', views.services),
    path('products/', views.products),
    path('faq/', views.faq),
    path('contacts/', views.contacts),
]