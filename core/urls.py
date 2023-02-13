from django.urls import path, re_path
from . import views
urlpatterns = [
    #path('',  views.redirect_to_url_main_page, name=''),
    path('main_page/', views.base, name='main_page'),

]