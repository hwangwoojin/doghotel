from django.shortcuts import render, redirect
from django.db.models import Count
from .models import user, dog

# Create your views here.

def mypage(request):
    # if first, create new database
    if user.objects.filter(id=request.user).count() == 0:
        _user = user(id=request.user)
        _user.save()
    # get userinfo from queryset
    userinfo = user.objects.get(id=request.user)
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
        return render(request, 'mypage/mypage.html', {'userinfo': userinfo})

def mydog(request):
    # doglist
    doginfo = dog.objects.filter(userid=str(request.user))
    return render(request, 'mypage/mydog.html', {'doginfo': doginfo})

def mydogAdd(request):
    # POST
    if request.method == 'POST':
        # insert database
        _dog = dog()
        _dog.userid = str(request.user)
        _dog.name = request.POST['name']
        _dog.breed = request.POST['breed']
        _dog.age = request.POST['age']
        _dog.weight = request.POST['weight']
        _dog.feature= request.POST['feature']
        _dog.save()
        return redirect('mydog')
    # GET
    else:
        # get userinfo from queryset
        return render(request, 'mypage/mydogAdd.html')