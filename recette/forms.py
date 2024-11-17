from dal import autocomplete
from django import forms

from recette.models import Recette, ListeIngredients, Ingredient, Batch, Categorie

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ('__all__')
        widgets = {
            'reference': autocomplete.ModelSelect2(url='source-autocomplete'),
            #'batch': autocomplete.ModelSelect2(url='batch-autocomplete'),
            'categories': autocomplete.ModelSelect2Multiple(url='categorie-autocomplete'),
        }

class ListeIngredientForm(forms.ModelForm):
    class Meta:
        model = ListeIngredients
        fields = ('ingredient', 'quantite','unite')
        widgets = {
            'ingredient': autocomplete.ModelSelect2(url='ingredient-autocomplete'),
        }

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ('nom', 'recette','jour')
    
    def __init__(self, *args, **kwargs):
        super(BatchForm, self).__init__(*args, **kwargs)
        self.fields['recette'].queryset = Recette.objects.filter(is_batch=True)
    
class SearchBar(forms.Form):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='ingredient-autocomplete',
            ),
        required=False)
    
    # categorie = forms.ChoiceField(choices=Recette.Categorie.choices,
    #     required=False)
    
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        # widget=autocomplete.ModelSelect2Multiple(
        #     url='ingredient-autocomplete',
        #     ),
        required=False)

    