from django.shortcuts import render
from django.shortcuts import render


def home(request):
    context = {
        'h1': 'Recipes',
        'title': 'Home'
    }
    return render(request, 'pages/home.html', context)


def contact(request):
    context = {
        'title': 'Contato'
    }
    return render(request, 'pages/contact.html', context)


def about(request):
    context = {
        'title': 'Sobre'
    }
    return render(request, 'pages/about.html', context)
