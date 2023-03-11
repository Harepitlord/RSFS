"""hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views

app_name='hub'
urlpatterns = [
    path('',views.Home.as_view(),name='Home'),
    path('home',views.DashBoard.as_view(),name='Dashboard'),
    path('about',views.About.as_view(),name='About'),
    path('makeShipment',views.NewShipment.as_view(),name='NewShipment'),

    path('shipper/home',views.ShipperDashboard.as_view(),name='ShipperDashboard'),
    path('logistics/home',views.LogisticsDashboard.as_view(),name='LogisticsDashboard'),

]
