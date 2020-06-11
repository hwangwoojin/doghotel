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
    # if first, create new database
    if dog.objects.filter(id=request.user).count() == 0:
        _dog = dog(id=request.user)
        _dog.save()
    # get userinfo from queryset
    doginfo = dog.objects.get(id=request.user)
    # POST
    if request.method == 'POST':
        # update database
        doginfo.name = request.POST['name']
        doginfo.breed = request.POST['breed']
        doginfo.age = request.POST['age']
        doginfo.weight = request.POST['weight']
        doginfo.save()
        return redirect('home')
    # GET
    else:
        return render(request, 'mypage/mydog.html', {'doginfo': doginfo})