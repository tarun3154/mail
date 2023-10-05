from django import forms
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions']


class IngredientForm(forms.ModelForm):
    class Meta:
        model=Ingredient
        fields=['name']