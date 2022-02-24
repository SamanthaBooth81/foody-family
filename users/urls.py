"""Accounts urls"""
from django.urls import path
from django.contrib.auth import views
from users import views as user_views


urlpatterns = [

    path('register',
         user_views.register_user, name='register'),
     path('login/',
         user_views.login_page, name='login'),

    # https://stackoverflow.com/questions/14021913/django-logout-not-working
    # to find below url path
    path('logout/',
         views.LogoutView.as_view(next_page='/'), name="logout"),

    path('change-password',
         user_views.change_password, name='change_password'),
]
