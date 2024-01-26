from django.shortcuts import render
from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'pages/home.html', context)


def recipe(request, id):
    context = {
        'title': 'Recipe',
    }
    return render(request, 'pages/recipe.html', context)
