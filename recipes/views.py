"""Views for the different pages to be rendered"""
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.utils.text import slugify
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm


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


def AddRecipe(request):
    """Allows user to add a recipe"""
    recipe_form = RecipeForm(data=request.POST)

    if recipe_form.is_valid():
        recipe = recipe_form.save(commit=False)
        recipe.author_id = request.user.id
        recipe.slug = slugify(recipe.title)
        recipe.save()
    else:
        recipe_form = RecipeForm()
        return render(
            request,
            "add_recipe.html",
            {
                "recipe_form": recipe_form,
            },
        )
    return redirect('home')


class UserRecipes(generic.ListView):
    """View for the list of recipes posted"""
    model = Recipe
    template_name = 'my_recipes.html'
