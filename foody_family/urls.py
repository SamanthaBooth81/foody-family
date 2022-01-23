"""foody_family URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('recipes.urls'), name='recipe_urls'),

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

]
