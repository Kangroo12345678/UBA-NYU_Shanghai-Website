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
    context = {
        'member_list': member_list,
    }
    return render(request, template, context)
    #HttpResponse(template.render(context, request))


