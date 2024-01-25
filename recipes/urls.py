from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('about', views.about, name='about'),
]
