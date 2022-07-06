from dal import autocomplete
from django import forms

from recette.models import Recette, ListeIngredients, Ingredient

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ('__all__')
        widgets = {
            'reference': autocomplete.ModelSelect2(url='source-autocomplete'),
            'batch': autocomplete.ModelSelect2(url='batch-autocomplete'),
        }

class ListeIngredientForm(forms.ModelForm):
    class Meta:
        model = ListeIngredients
        fields = ('ingredient', 'quantite','unite')
        widgets = {
            'ingredient': autocomplete.ModelSelect2(url='ingredient-autocomplete'),
        }
        
class SearchBar(forms.Form):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='ingredient-autocomplete',
            ))

    