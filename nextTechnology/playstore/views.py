from django.shortcuts import render,HttpResponse,redirect
from .models import AppAdmin
import play_scraper
from django.contrib import messages

# Admin user and password
# It should be taken from json 
adminUser='anonymous'
adminPass='securepassword@123'





# Taking required information from the details
def details(request):
    # If we make a search request and 
    if 'Search' in request.GET:
        query=request.GET['Search']
        # Searches using play scraper module
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
def adminPage(request):
    # take the details
    app=details(request) 
    # If session has a user and if it is admin then return the admin page
    if request.session.has_key('username') and request.session['username']==adminUser:
        # If request has made to add app         
        if request.method=='POST':
            pointfromPage=request.POST['points']
            categoryfromPage=request.POST['category']
            currdownloadLink='https://play.google.com'+app[3]
            # creates an app object and saves it
            if AppAdmin.objects.filter(name=app[0]).exists():
                messages.warning(request,'App already exists!!')
                passToHtml={
                      'title':'Admin Home',
                      'app_status': False,
                    }
            else:
                createObject=AppAdmin(name=app[0],appID=app[1],iconLink=app[2],downloadLink=currdownloadLink,category=categoryfromPage,points=pointfromPage)  
                createObject.save()
                # sends the success message
                messages.success(request,'App added successfully!!')
                passToHtml={
                      'title':'Admin Home',
                      'app_status': False,
                    }
        else:     
            # If app returns list then pass it to admin page   
            if app:
                passToHtml={
                    'title':'Admin Home',
                    'app_name': app[0],
                    'app_id': app[1],
                    'app_icon':app[2],
                    'app_status':True,
                    'categories':app[4],
                }
            else:
                passToHtml={
                    'title':'Admin Home',
                    'app_status': False,
                }
        return render(request,'adminPage.html',passToHtml)
    return redirect('admin-login')














# If anyone searches for apps page then redirect him here
def apps(request):
    #If the user in session then only give him this page
    if request.session.has_key('username') and request.session['username']==adminUser:
        # Take all object and display it
        app_list=AppAdmin.objects.all()
        # Delete if a POST request comes
        if request.method=='POST':
            currentappID=request.POST['app']
            deleteObject=AppAdmin.objects.get(id=currentappID)
            deleteObject.delete()
        passToHtml={
            'title':'Added Apps',
            'app_list':app_list,            }
        return render(request,'apps.html',passToHtml)
    else:
        return redirect('admin-login')







# If login page is requested then it will come here
def adminLogin(request):
    # If he is already logged in don't ask him again 
    if request.session.has_key('username'):
        return redirect('admin/')
    else:
        if request.method=='POST':
            inputUser=request.POST['username']
            inputPass=request.POST['password']
            # If that is same as the admin user then redirect him to login page
            if inputUser==adminUser and inputPass==adminPass:
                request.session['username']=adminUser
                return redirect('admin/')
            # else send a warning flash-message that user Not found 
            else:
                messages.warning(request,'Not found')
        return render(request,'adminLogin.html')









# If log-out is requested then it will delete the session variable and redirects to login page
def logout(request):
    try:
        del request.session['username']
        return redirect('admin-login')
    except:
        return HttpResponse("<h1 style='margin:50px; font-size:80px;'><b>404 Not Found</b></h1>")