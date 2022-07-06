from django.urls import path
from recette.viewsautocomplete import IngredientAutocomplete, BatchAutocomplete

urlpatterns = [
        path('ingredient-autocomplete/', IngredientAutocomplete.as_view(), name='ingredient-autocomplete'),
        path('batch-autocomplete/', BatchAutocomplete.as_view(), name='batch-autocomplete')
]