"""Projet_locationimmo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>', views.liste_clients, name='client'),
    path('ajout_client/', views.ajouter_client, name='ajout_client'),
    path('update_client/<str:pk>/', views.update_client, name='update_client'),
    path('delete_client/<str:pk>/', views.delete_client, name='delete_client'),
]
