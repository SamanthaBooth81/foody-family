"""Views for the different pages to be rendered"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


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
    """User Registration"""
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, username=username, password=password)
        login(request, user)
        return redirect('login')
    else:
        messages.info(request, 'Please ensure the password matches')
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})
