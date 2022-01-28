from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="recipe_detail"),
    path("templates/add_recipe/", views.AddRecipe, name="add_recipe"),
    path("templates/my_recipes/",
         views.UserPostedRecipes.as_view(), name="my_posted_recipes"),
    path("templates/my_drafts/",
         views.UserDraftRecipes.as_view(), name="my_draft_recipes"),
    path("update_recipe/<int:pk>",
         views.UpdateRecipe.as_view(), name="update_recipe"),
]
