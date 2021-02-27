from django.urls import path
from .views import admin,apps

urlpatterns=[
    path('',admin,name='playstore-home'),
    path('apps/',apps,name='playstore-apps'),
]