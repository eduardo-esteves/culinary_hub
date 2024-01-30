from django.shortcuts import render
from django.shortcuts import render

from utils.recipes.factory import make_recipe

def home(request):
    context = {
        'title': 'Home',
        'recipes': [make_recipe() for _ in range(6)],
    }
    return render(request, 'pages/home.html', context)


def recipe(request, id):
    context = {
        'title': 'Recipe',
        'recipe': make_recipe(),
    }
    return render(request, 'pages/recipe.html', context)
