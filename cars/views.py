from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

# Create your views here.

#def index(request):
#   return HttpResponse("Welcome to PimpMycars.")

def listCar(request, carid ):
    response = "You're looking at the list of cars"

def index(request):
    car_list = Car.objects.order_by('years')[:5]
    context = {'car_list': car_list}
    return render(request, 'cars/index.html', context)