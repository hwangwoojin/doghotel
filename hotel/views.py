from django.shortcuts import render, redirect
from .models import hotels

# Create your views here.

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