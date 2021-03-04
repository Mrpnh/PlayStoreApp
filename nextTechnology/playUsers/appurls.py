from  django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register/',userRegister,name='user-register'),
    path('',auth_views.LoginView.as_view(template_name='playUsers/userLogin.html'),name='user-login'),
    path('logout/',auth_views.LogoutView.as_view(),name='user-logout'),
    path('userhome/',userHome,name='user-home'),
    path('userprofile/',userProfile,name='user-profile'),
    path('userhome/<int:currid>/',userPage,name='user-page'),
]