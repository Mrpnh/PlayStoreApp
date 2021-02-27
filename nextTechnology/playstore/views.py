from django.shortcuts import render,HttpResponse

# Python's scrapping module to scrap info from playstore
import play_scraper


# Gets the Details of the searched app 
def details(request):
    query=request.POST['Search']
    appDetails=play_scraper.search(query)[0]
    # Taking required information from the details
    appName=appDetails['title']
    appId=appDetails['app_id']
    downloadURL=appDetails['url']
    icon=appDetails['icon']
    return [appName,appId,icon,downloadURL]


# Create your views here.
def admin(request):
    app=details(request)
    passToHtml={
        'title':'Admin Home',
        'app_name': app[0],
        'app_id': app[1],
        'app_icon':app[2],
        }
    return render(request,'adminPage.html',passToHtml)

def apps(request):
    passToHtml={
        'title':'Added Apps',
        }
    return render(request,'apps.html',passToHtml)