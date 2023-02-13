from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',  views.featured_product_view, name=''),
    path('main_page/', views.index, name='main_page'),

]