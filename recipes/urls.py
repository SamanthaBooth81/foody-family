from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="recipe_detail"),
    path("templates/add_recipe/", views.AddRecipe, name="add_recipe")
]
