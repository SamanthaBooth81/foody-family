from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'preparation_length', 'cooking_length',
                  'total_length', 'ingredients', 'instructions',
                  'featured_image', 'excerpt',)