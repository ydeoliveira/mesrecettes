from django.urls import path
from recette.viewsautocomplete import IngredientAutocomplete, BatchAutocomplete, RecetteAutocomplete, CategorieAutocomplete
from recette.views import Ingredient, Recettes, VueRecette

urlpatterns = [
        path('ingredient/', Ingredient.as_view(), name='ingredient'),
        path('recettes/', Recettes.as_view(), name='recettes'),
        path('recette/<int:pk>', VueRecette.as_view(), name='recette'),
        path('ingredient-autocomplete/', IngredientAutocomplete.as_view(), name='ingredient-autocomplete'),
        path('batch-autocomplete/', BatchAutocomplete.as_view(), name='batch-autocomplete'),
        path('recette-autocomplete/', RecetteAutocomplete.as_view(), name='recette-autocomplete'),
        path('categorie-autocomplete/', CategorieAutocomplete.as_view(), name='categorie-autocomplete')
]