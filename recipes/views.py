from django.shortcuts import render
from django.shortcuts import render

from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    context = {
        'title': 'Home',
        'recipes': recipes,
    }
    return render(request, 'pages/home.html', context)


def recipe(request, id):
    context = {
        'title': 'Recipe',
        'recipe': make_recipe(),
    }
    return render(request, 'pages/recipe.html', context)
