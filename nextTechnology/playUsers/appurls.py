from  django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .api.views import apiAppView

urlpatterns=[
    # registers the user
    path('register/',userRegister,name='user-register'),
    # go to login page
    path('',auth_views.LoginView.as_view(template_name='playUsers/userLogin.html'),name='user-login'),
    # logouts the user
    path('logout/',auth_views.LogoutView.as_view(),name='user-logout'),
    # go to user home
    path('userhome/',userHome,name='user-home'),
    # go to user profile
    path('userprofile/',userProfile,name='user-profile'),
    # go to user page
    path('userhome/<int:currid>/',userPage,name='user-page'),
    #API for user
    path('api/',apiAppView,name='user-api'),
]