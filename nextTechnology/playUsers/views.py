from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from playUsers.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from playstore.models import AppAdmin

# Create your views here.
def userRegister(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            curruser=User.objects.get(username=request.POST['username'])
            pro=Profile(user=curruser)
            pro.save()
            messages.success(request,'Account Created Successfully!!')
            return redirect('user-login')
    else:
        form=UserRegisterForm()
    return render(request,'playUsers/userRegister.html',{'form':form,'title':'Admin Register'})

@login_required
def userHome(request):
    applist=AppAdmin.objects.all()
    currUser=User.objects.get(username=request.user)
    pro=Profile.objects.get(user=currUser)
    passtoHTML={
        'title':'Home',
        'applist':applist,
        'downloadedApps':pro.downloaded,
    }
    return render(request,'playUsers/userHome.html',passtoHTML)

@login_required
def userProfile(request):
    if request.method=='POST':
        currentUsername=request.POST['username']
        currentUser=User.objects.get(username=currentUsername)
        currentUser.set_password(request.POST['newpassword'])
        currentUser.save()
        messages.success(request,'Password Changed Successfully!! Login Again')
        return redirect('user-login')
    return render(request,'playUsers/userProfile.html',{'title':'Profile'})

@login_required
def userPage(request,currid):
    currapp=AppAdmin.objects.get(id=currid)
    passtoHTML={
        'currapp':currapp,     
    }
    if request.method=='POST':
        curruser=User.objects.get(username=request.POST['curruser'])
        pro=Profile.objects.get(user=curruser)
        pro.points+=int(request.POST['point'])
        pro.tasks+=1
        pro.downloaded.append(request.POST['downloaded'])
        pro.screenshot=request.POST['file']
        pro.save()
        messages.success(request,'Task Completed Successfully!!')
        return redirect('user-home')
    return render(request,'playUsers/userPage.html',passtoHTML)