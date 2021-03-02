from django.urls import path
from .views import apps,adminLogin,adminPage,logout


urlpatterns=[
    # Go to admin register page
    path('',adminLogin,name='admin-login'),
    # Go to apps page where all added apps are there
    path('apps/',apps,name='admin-apps'),
    # Go to admin home page
    path('admin/',adminPage,name='admin-home'),
    # Go to logout page
    path('logout',logout,name='admin-logout'),
]