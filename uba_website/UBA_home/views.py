from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import member, event
# Create your views here.


# def home_view(request):
#     return render(request, 'home/home.html')

# def events_view(request):
#     return render(request, 'events/events.html')


# def home_view(request):
# return HttpResponse("Welcome to UBA Home!")

# def events_view(request):
# return HttpResponse("View our past and upcoming events!")


def home(request):
    member_list = member.objects.all()
    output = "----------------------------------".join([str(q) for q in member_list])
    template = 'intro.html'
    new = []

    for mem in member_list:
        if mem.role == 'President':
            new.append(mem)

    for mem in member_list:
        if new != [] and mem.role == 'Vice President':
            new.append(mem)
    for mem in member_list:
        if 'Director' in mem.role:
            new.append(mem)

    for mem in member_list:
        if 'Treasure' in mem.role:
            new.append(mem)

#""" I have to admit that this is not good code. It is meant to make the system automatically generate the list of executive members in the right 
#sequence to show on the website"""


    member_list = new

    context = {
        'member_list': member_list,
    }
    return render(request, template, context)
    #HttpResponse(template.render(context, request))


