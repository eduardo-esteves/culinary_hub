from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>', views.recipe, name='recipes'),
    path('recipes/category/<int:category_id>', views.category, name='categories'),
]
