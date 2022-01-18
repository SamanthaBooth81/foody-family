"""Views for the different pages to be rendered"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Recipe



class RecipeList(generic.ListView):
    """View for the list of recipes posted"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12


class RecipeDetail(View):
    """View recipe details"""

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        # comments = recipe.comments.filter
        # (approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                # "comments": comments,
                "liked": liked
            },
        )


# Code from Dennis Ivy YouTube Video, link in README
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
    
    context = {}

    return render(request, 'accounts/login.html', context)

