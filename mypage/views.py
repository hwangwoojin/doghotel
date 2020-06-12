from django.shortcuts import render, redirect
from django.db.models import Count
from .models import user, dog, hotels, reservations

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
        return redirect('hotel')
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

def hotel(request):
    hotelinfo = hotels.objects.all()
    return render(request, 'hotel/hotel.html', {'hotelinfo': hotelinfo})

def hotelAdd(request):
    # POST
    if request.method == 'POST':
        # insert database
        _hotel = hotels()
        _hotel.userid = str(request.user)
        _hotel.name = request.POST['name']
        _hotel.location = request.POST['location']
        _hotel.homepage = request.POST['homepage']
        _hotel.phone = request.POST['phone']
        _hotel.rate= request.POST['rate']
        _hotel.save()
        return redirect('hotel')
    # GET
    else:
        # get userinfo from queryset
        return render(request, 'hotel/hotelAdd.html')

def hotelRate(request):
    hotelinfo = hotels.objects.all().order_by('-rate')
    return render(request, 'hotel/hotel.html', {'hotelinfo': hotelinfo})

def hotelNameSearch(request):
    _name = request.POST['name']
    hotelinfo = hotels.objects.filter(name__contains=str(_name))
    return render(request, 'hotel/hotel.html', {'hotelinfo': hotelinfo})

def hotelLocationSearch(request):
    _location = request.POST['location']
    hotelinfo = hotels.objects.filter(location__contains=str(_location))
    return render(request, 'hotel/hotel.html', {'hotelinfo': hotelinfo})

def reservation(request):
    _reservation = reservations()
    _reservation.managerid = request.POST['userid']
    _reservation.userid = str(request.user)
    _reservation.save()
    return redirect('hotel')