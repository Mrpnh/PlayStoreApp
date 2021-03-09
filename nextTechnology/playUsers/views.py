from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from playUsers.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from playstore.models import AppAdmin
from rest_framework.authtoken.models import Token



# New User registers here
def userRegister(request):
    # If a request is POSTED
    if request.method=='POST':
        # Uses Instance of django UsercreationFrom to create a form
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            # save the form
            form.save()
            # gets the current user
            curruser=User.objects.get(username=request.POST['username'])
            # And creates a profile for him which contains points,tasks etc. 
            pro=Profile(user=curruser)
            # saves the profile
            pro.save()
            # Create the token for that perticular object
            Token.objects.create(user=curruser) 
            # Sends the success message and redirects to login page
            messages.success(request,'Account Created Successfully!!')
            return redirect('user-login')
    else:
        # else creates a blank form
        form=UserRegisterForm()
    return render(request,'playUsers/userRegister.html',{'form':form,'title':'Admin Register'})







# Uses decorator login_required to verify user login
@login_required
def userHome(request):
    # Gets all the apps
    applist=AppAdmin.objects.all()
    # Gets the current user
    currUser=User.objects.get(username=request.user)
    # gets the profile page
    pro=Profile.objects.get(user=currUser)
    # Gets the current user
    curruser=User.objects.get(username=request.user)
    # Gets the token of that user
    token=Token.objects.filter(user=curruser).first()
    passtoHTML={
        'title':'Home',
        'applist':applist,
        'downloadedApps':pro.downloaded,
        'token':token,
    }
    return render(request,'playUsers/userHome.html',passtoHTML)









@login_required
# User profile page
def userProfile(request):
    # Gets the current user
    curruser=User.objects.get(username=request.user)
    # gets the token of that user
    token=Token.objects.filter(user=curruser).first()
    # If a request is made to change the password
    if request.method=='POST':
        currentUsername=request.POST['username']
        # takes the current user
        currentUser=User.objects.get(username=currentUsername)
        # changes password
        currentUser.set_password(request.POST['newpassword'])
        # save the password
        currentUser.save()
        # sends the success message and redirects to login-page
        
        messages.success(request,'Password Changed Successfully!! Login Again')
        return redirect('user-login')
    return render(request,'playUsers/userProfile.html',{'title':'Profile','token':token,})











@login_required
def userPage(request,currid):
    # Gets the current app using its id
    currapp=AppAdmin.objects.get(id=currid)
    passtoHTML={
        'currapp':currapp,  
        'title':'User Page',   
    }
    # If a request is made to complete the task
    if request.method=='POST':
        curruser=User.objects.get(username=request.POST['curruser'])
        # Gets the profile of the page
        pro=Profile.objects.get(user=curruser)
        # Increases the point
        pro.points+=int(request.POST['point'])
        # increses the task
        pro.tasks+=1
        # appends the file downloaded
        pro.downloaded.append(request.POST['downloaded'])
        # uploaded file is saved
        pro.screenshot=request.POST['file']
        pro.save()
        messages.success(request,'Task Completed Successfully!!')
        # redirects to home page
        return redirect('user-home')
    return render(request,'playUsers/userPage.html',passtoHTML)