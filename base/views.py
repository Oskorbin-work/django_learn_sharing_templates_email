from django.shortcuts import render, redirect
from .models import Base
from .models import ContentBody
from django.utils.translation import get_language

def main_page(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Main Page")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1]
    }
    return render(request, 'main_page.html', context=context)

def about_me_education(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Education")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1]
    }
    return render(request, 'about_me/education.html', context=context)

def about_me_skills(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Skills")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1]
    }
    return render(request, 'about_me/skills.html', context=context)

def about_me_languages(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Languages")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1]
    }
    return render(request, 'about_me/languages.html', context=context)

def about_me_hobbies(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Hobbies")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1]
    }
    return render(request, 'about_me/hobbies.html', context=context)

def contacts(request):
    base_entry = Base.objects.all()[0]
    content_body = ContentBody.objects.filter(translations__title="Contacts")[0]
    context = {
        'Base': base_entry,
        "Content_body": content_body,
        'get_last_url': request.path[4:-1]
    }
    return render(request, 'contacts.html', context=context)


def redirect_to_url_main_page(request):
    return redirect("/"+get_language()+'/main_page/')
