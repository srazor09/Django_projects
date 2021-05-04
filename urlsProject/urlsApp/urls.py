from django.contrib import admin
from django.urls import path
from urlsApp import views

urlpatterns = [
    path('hydjobs/', views.hydjobsInfo),
    path('punejobs/', views.punejobsInfo),
    path('mumbaijobs/', views.mumbaijobsInfo),
    path('noidajobs/', views.noidajobsInfo),
]
