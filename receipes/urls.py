from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_ingredients/', views.add_ingredients, name='add_ingredients'),

    # Define URLs for editing and deleting recipes.
]
