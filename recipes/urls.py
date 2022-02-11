from django.urls import path
from . import views


urlpatterns = [
    path("add-recipe/", views.AddRecipe, name="add_recipe"),
    path("my-recipes/",
         views.UserPostedRecipes.as_view(), name="my_posted_recipes"),
    path("pending-approval/",
         views.ApprovalPendingRecipes.as_view(), name="my_pending_recipes"),
    path("pending-approval/<int:pk>",
         views.DraftRecipeDetail.as_view(), name="draft_recipe_detail"),
    path("my-recipes/update-recipe/<int:pk>",
         views.UpdateRecipe.as_view(), name="update_recipe"),
    path("my-recipes/delete-recipe/<int:pk>",
         views.DeleteRecipe.as_view(), name="delete_recipe"),
    path("my-recipes/update-pending-recipe/<int:pk>",
         views.UpdatePendingRecipe.as_view(), name="update_draft"),
    path("my-recipes/delete-pending-recipe/<int:pk>",
         views.DeletePendingRecipe.as_view(), name="delete_draft"),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="recipe_detail"),
    path("like/<slug:slug>/", views.RecipeLike.as_view(), name="recipe_like")
]
