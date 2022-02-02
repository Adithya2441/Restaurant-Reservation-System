from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('authenticate_login/',views.authenticate_login,name='authenticate_login'),
    path('main/',views.main_page,name='main_page'),
    path('main/booknow/',views.book_now,name='booknow'),
    path('main/menu/',views.menu,name='menu'),
    path('main/booknow/confirmed/<str:id>',views.confirmed,name='confirmed'),
    path('main/booknow/delete/<str:id>',views.delete_booking,name='delete'),
    path('main/booknow/update/<str:id>',views.update_booking,name='update'),
]