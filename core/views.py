from django.shortcuts import render, redirect
from .models import Base

def base(request):
    all_test = Base.objects.all()
    context = {
        #'all_destination': all_destination,
        'Base': all_test,
        'get_last_url':request.path.split("/",-1)[-2]
    }
    return render(request, 'base.html', context=context)

def redirect_to_url_main_page(request):
    return redirect('/main_page/')
