from django.shortcuts import render, redirect
from .models import user

# Create your views here.

def mypage(request):
    # get userinfo from queryset
    userinfo = user.objects.get(id='hwangwoojin')
    # POST
    if request.method == 'POST':
        # update database
        userinfo.name = request.POST['name']
        userinfo.email = request.POST['email']
        userinfo.phone = request.POST['phone']
        userinfo.save()
        return redirect('home')
    # GET
    else:
        userinfo = user.objects.get(id='hwangwoojin')
        return render(request, 'mypage/mypage.html', {'userinfo': userinfo})

def mydog(request):
    return render(request, 'mypage/mydog.html')