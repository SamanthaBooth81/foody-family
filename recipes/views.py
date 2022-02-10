"""Views for the different pages to be rendered"""
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import UpdateView, DeleteView
from django.views import generic, View
from django.utils.text import slugify
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm


class RecipeList(generic.ListView):
    """View for the list of recipes posted by all users"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12


class RecipeDetail(View):
    """View recipe details"""

    def get(self, request, slug, *args, **kwargs):
        """Function to get the recipe details"""
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "liked": liked
            },
        )


class RecipeLike(View):
    """View for the likes function"""

    def post(self, request, slug, *args, **kwargs):
        """Likes function, display if user has/hasn't liked recipe"""
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def AddRecipe(request):
    """View for user to add a recipe"""
    recipe_form = RecipeForm(data=request.POST)
    print(request.POST)
        
    if recipe_form.is_valid():
        recipe = recipe_form.save(commit=False)
        """Post on Stack Overflow in README for appending array to field"""
        recipe.instructions = []
        instruction = request.POST.getlist('instructions')
        recipe.instructions.append(instruction)
        recipe.author_id = request.user.id
        recipe.slug = slugify(recipe.title)
        messages.success(
            request, "Recipe submitted and waiting approval!")
        recipe.save()
        return redirect('home')
    else:
        return render(
            request,
            "add_recipe.html",
            {
                "recipe_form": recipe_form,
            },
        )
    return render(request, "add_recipe.html",
                  {
                      "recipe_form": recipe_form,
                  },
                  )


class UserPostedRecipes(generic.ListView):
    """View for the list of recipes posted"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = 'my_recipes.html'
    paginate_by = 12


class ApprovalPendingRecipes(generic.ListView):
    """View for the list of recipes pending"""
    model = Recipe
    queryset = Recipe.objects.filter(status=0)
    template_name = 'my_drafts.html'
    paginate_by = 12


class UpdateRecipe(UpdateView):
    """View to update published recipes"""
    model = Recipe
    form = RecipeForm()
    fields = ['title', 'preparation_length', 'cooking_length',
              'total_length', 'ingredients', 'instructions',
              'featured_image', 'excerpt', ]
    template_name = 'update_recipe.html'
    success_url = reverse_lazy('my_posted_recipes')


class DeleteRecipe(DeleteView):
    """View to delete published recipes"""
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('my_posted_recipes')


class UpdatePendingRecipe(UpdateView):
    """View to update pending recipes"""
    model = Recipe
    form = RecipeForm()
    fields = ['title', 'preparation_length', 'cooking_length',
              'total_length', 'ingredients', 'instructions',
              'featured_image', 'excerpt', ]
    template_name = 'update_recipe.html'
    success_url = reverse_lazy('my_pending_recipes')


class DeletePendingRecipe(DeleteView):
    """View to delete pending recipes"""
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('my_pending_recipes')
