from django.urls import path
# from . import views
# from django.contrib import admin
from django.contrib.auth import views
from users import views as user_views


urlpatterns = [

    path('accounts/login/register',
         user_views.RegisterUser, name='register'),

    # Django Auth - help from Hacker Shack Video in README for login path
    path('accounts/login/',
         views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),

    # https://stackoverflow.com/questions/14021913/django-logout-not-working
    # to find below url path
    path('accounts/logout/',
         views.LogoutView.as_view(next_page='/'), name="logout"),

    path('accounts/profile/', user_views.UserProfile, name='profile'),

    path('accounts/manage_account/',
         user_views.ManageAccount, name='manage_account'),

    path('accounts/change_password',
         user_views.ChangePassword, name='change_password'),

    path('accounts/password_success/',
         user_views.PasswordSuccess, name='password_change_done'),

    path('accounts/manage_account/confirm_delete_account/',
         user_views.DeleteAccount, name='confirm_delete_account')
]
