from django.urls import path
from . import views
urlpatterns = [
    path('',  views.redirect_to_url_main_page, name=''),
    path('main_page/', views.main_page, name='main_page'),
    path('about_me/education/',  views.about_me_education, name='about_me_education'),
    path('about_me/skills/', views.about_me_skills, name='about_me_skills'),
    path('about_me/languages/', views.about_me_languages, name='about_me_languages'),
    path('about_me/hobbies/',  views.about_me_hobbies, name='about_me_hobbies'),
    path('contacts/', views.contacts, name='contacts'),

]