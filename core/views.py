
from django.shortcuts import render
from .models import Base

def index(request):
    all_test = Base.objects.all()
    context = {
        #'all_destination': all_destination,
        'Base': all_test,
    }
    return render(request, 'base.html', context=context)
