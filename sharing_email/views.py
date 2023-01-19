from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

def index(request):
    all_destination = Destination.objects.all()
    context = {
        'all_destination': all_destination,
    }
    return render(request, 'base.html', context=context)