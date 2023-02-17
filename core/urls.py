from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',  views.redirect_to_url_main_page, name=''),
    path('contacts/',  views.redirect_to_url_main_page, name='contacts'),
    path('about_me/education/',  views.redirect_to_url_main_page, name='about_me_education'),
    path('about_me/hobbies/',  views.redirect_to_url_main_page, name='about_me_hobbies'),
    path('about_me/languages/',  views.redirect_to_url_main_page, name='about_me_languages'),
    path('about_me/skills/',  views.redirect_to_url_main_page, name='about_me_skills'),
    path('projects/sharing_emails/',  views.redirect_to_url_main_page, name='projects_sharing_emails'),
    path('main_page/', views.base, name='main_page'),

]