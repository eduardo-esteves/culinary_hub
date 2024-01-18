from django.shortcuts import render
from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home.html', context)


def contact(request):
    context = {
        'title': 'Contato'
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'title': 'Sobre'
    }
    return render(request, 'about.html', context)
