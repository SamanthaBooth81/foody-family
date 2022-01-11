"""admin file for database set up"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """User summernote text fields for ingredients and instructions"""
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    # research how to search by author (author is currently a Foreign Key)
    search_fields = ('title', 'ingredients')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')
