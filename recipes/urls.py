from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="recipe_detail"),
    path("templates/add_recipe/", views.AddRecipe, name="add_recipe"),
    path("templates/my_recipes/",
         views.UserPostedRecipes.as_view(), name="my_posted_recipes"),
    path("templates/my_drafts/",
         views.ApprovalPendingRecipes.as_view(), name="my_pending_recipes"),
    path("my_recipes/update_recipe/<int:pk>",
         views.UpdateRecipe.as_view(), name="update_recipe"),
     path("my-recipes/delete-recipe/<int:pk>",
         views.DeleteRecipe.as_view(), name="delete_recipe"),
]

