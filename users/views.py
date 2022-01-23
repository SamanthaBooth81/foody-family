"""Views for the different pages to be rendered"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def LoginPage(request):
    """User Login View"""
    # Code from Dennis Ivy YouTube Video, link in README, and amended slightly
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user.is_valid():
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}

    return render(request, 'accounts/login.html', context)


def LogoutUser(request):
    """User Logout View"""
    # Used Django documentation for this view
    # https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-out
    logout(request)
    return redirect('home')


def RegisterUser(request):
    """User Registration Form View.
    Used The Pylot article to help create this view.
    Link in README"""

    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, username=username, password=password)
        login(request, user)
        messages.success(request, "Welcome {{ user.username }}!")
        return redirect('home')
    else:
        messages.error(request, 'Please ensure the password matches')
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def UserProfile(request):
    """View to see users profile page"""
    return render(request, 'accounts/profile.html')


def ManageAccount(request):
    """View to see users profile page"""
    return render(request, 'accounts/manage_account.html')


def ChangePassword(request):
    """Manage User Account to Change Password and Delete Account"""
    #  Used Professional Cipher Youtube video to help with the
    # change password view
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
        # messages.success(request, "Password Updated")
        update_session_auth_hash(request, form.user)
        return redirect('password_change_done')
    else:
        messages.error(request, 'Please correct the error.')

    return render(request, 'accounts/change_password.html', {'form': form})


def PasswordSuccess(request):
    """Password Update Success Message"""
    return render(request, 'accounts/password_success.html')
