from django.shortcuts import render, redirect
from .models import Base
from .models import ContentBody
from django.utils.translation import get_language

def base(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Main Page")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path.split("/", -1)[-2]
    }
    return render(request, 'main_page.html', context=context)


def redirect_to_url_main_page(request):
    return redirect("/"+get_language()+'/main_page/')
