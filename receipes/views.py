from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'receipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'receipes/recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'receipes/add_recipe.html', {'form': form})

def add_ingredients(request):
    if request.method== 'POST':
        form=IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form =IngredientForm()
    return render(request, 'receipes/ingredients.html',{'form':form})

