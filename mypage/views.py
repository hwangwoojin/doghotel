from django.shortcuts import render, redirect
from .models import user, dog

# Create your views here.

def mypage(request):
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
        userinfo = user.objects.get(id=request.user)
        return render(request, 'mypage/mypage.html', {'userinfo': userinfo})

def mydog(request):
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
        doginfo = dog.objects.get(id=request.user)
        return render(request, 'mypage/mydog.html', {'doginfo': doginfo})