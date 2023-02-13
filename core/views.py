from django.shortcuts import render, redirect
from .models import Base

def index(request):
    all_test = Base.objects.all()
    context = {
        #'all_destination': all_destination,
        'Base': all_test,
    }
    return render(request, 'base.html', context=context)

def featured_product_view(request):
    return redirect('/main_page/')
