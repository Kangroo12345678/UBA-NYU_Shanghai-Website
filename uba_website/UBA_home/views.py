from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render(request, 'home/home.html')

def events_view(request):
    return render(request, 'events/events.html')


# def home_view(request):
# return HttpResponse("Welcome to UBA Home!")

# def events_view(request):
# return HttpResponse("View our past and upcoming events!")

