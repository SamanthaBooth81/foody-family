from django.urls import path
# from . import views
# from django.contrib import admin
from django.contrib.auth import views
from users import views as user_views


urlpatterns = [

    path('register',
         user_views.RegisterUser, name='register'),

    # Django Auth - help from Hacker Shack Video in README for login path
    path('login/',
         views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),

    # https://stackoverflow.com/questions/14021913/django-logout-not-working
    # to find below url path
    path('logout/',
         views.LogoutView.as_view(next_page='/'), name="logout"),

    path('change_password',
         user_views.ChangePassword, name='change_password'),
]
