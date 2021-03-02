from django.shortcuts import render
from playstore.models import AppAdmin

# Create your views here.
def userpage(request):
    app_list=AppAdmin.objects.all()
    context={
        'applist':app_list,
    }
    return render(request,'userPage.html',context)
