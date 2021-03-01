from django.shortcuts import render,HttpResponse,redirect
from .models import AppAdmin
import play_scraper
from django.contrib import messages

adminUser='anonymous'
adminPass='securepassword@123'

# Taking required information from the details
def details(request):
    if 'Search' in request.GET:
        query=request.GET['Search']
        appDetails=play_scraper.search(query)[0]
        categories=list(play_scraper.categories().keys())
        if appDetails:
            appName=appDetails['title']
            appId=appDetails['app_id']
            downloadURL=appDetails['url']
            icon=appDetails['icon']
            return [appName,appId,icon,downloadURL,categories]
        else:
            return False
    return False


# Create your views here.

def adminPage(request,user):  
        app=details(request)
        if request.method=='POST':
            pointfromPage=request.POST['points']
            categoryfromPage=request.POST['category']
            createObject=AppAdmin(name=app[0],appID=app[1],iconLink=app[2],category=categoryfromPage,points=pointfromPage)  
            createObject.save()
            messages.success(request,'App added successfully!!')
            passToHtml={
                    'title':'Admin Home',
                    'app_status': False,
                    'path': f'/admin-register/admin/{user}',
                }
        else:          
            if app:
                passToHtml={
                    'title':'Admin Home',
                    'app_name': app[0],
                    'app_id': app[1],
                    'app_icon':app[2],
                    'app_status':True,
                    'path': f'/admin-register/admin/{user}',
                    'categories':app[4],
                }
            else:
                passToHtml={
                    'title':'Admin Home',
                    'app_status': False,
                    'path': f'/admin-register/admin/{user}',
                }
        return render(request,'adminPage.html',passToHtml)

def apps(request):
        app_list=AppAdmin.objects.all()
        if request.method=='POST':
            cuurentappID=request.POST['app']
            deleteObject=AppAdmin.objects.get(id=cuurentappID)
            deleteObject.delete()
        passToHtml={
            'title':'Added Apps',
            'app_list':app_list,
            'path': f'/admin-register/admin/{adminUser}',
            }
        return render(request,'apps.html',passToHtml)

def adminRegister(request):
    if request.method=='POST':
        inputUser=request.POST['username']
        inputPass=request.POST['password']
        if inputUser==adminUser and inputPass==adminPass:
            return redirect(f'admin/{adminUser}')
        else:
            messages.warning(request,'Not found')
    return render(request,'adminRegister.html')