"""iter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from trips import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/trips/', views.TripList.as_view()),
    path('api/trips/<int:pk>/', views.TripDetail.as_view()),
    path('api/trips/<int:trip_id>/destinations/', views.DestinationList.as_view()),
    path('api/trips/<int:trip_id>/destinations/<int:destination_id>/sites/', views.SiteList.as_view()),
    path('api/sites/<int:pk>/', views.SiteDetail.as_view()),
    path('api/trips/<int:trip_id>/destinations/<int:destination_id>/transportation/',
         views.TransportationList.as_view()),
    path('api/transportation/<int:pk>/', views.TransportationDetail.as_view()),
    path('api/trips/<int:trip_id>/destinations/<int:destination_id>/accommodations/',
         views.AccommodationList.as_view()),
    path('api/accommodations/<int:pk>/', views.AccommodationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
