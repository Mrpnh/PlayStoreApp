from django.urls import path
from .views import apps,adminRegister,adminPage


urlpatterns=[
    path('',adminRegister,name='admin-register'),
    path('apps/',apps,name='playstore-apps'),
    path('admin/<str:user>/',adminPage,name='playstore-home'),
]