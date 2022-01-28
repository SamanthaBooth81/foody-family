"""Django Models of foody-family databases"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """Django Model of recipe database"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post")
    updated_on = models.DateTimeField(auto_now=True)
    preparation_length = models.CharField(max_length=10, default=0)
    cooking_length = models.CharField(max_length=10, default=0)
    total_length = models.CharField(max_length=10, default=0)
    ingredients = models.TextField()
    instructions = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        """Orders posts by date created using descending order"""
        ordering = ['-created_on']

    def __str__(self):
        """Magic Method, returns a string representation of an object"""
        return self.title

    def number_of_likes(self):
        """Helper method, returns total count of likes on a recipe"""
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse('home')


# class Comments(models.Model):
#     """Django Model for comments database"""
#     post = models.ForeignKey(
#         Recipe, on_delete=models.CASCADE, related_name="comments")
#     name = models.CharField(max_length=80, unique=True)
#     email = models.EmailField()
#     body = models.TimeField()
#     created_on = models.BooleanField(default=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         """Orders posts by date created using ascending order"""
#         ordering = ['created_on']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"
