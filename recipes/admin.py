from django.contrib import admin

# Register your models here.
from recipes.models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
