from django import forms
from dal import autocomplete

from .models import MenuComposition

class MenuCompositionForm(forms.ModelForm):
    class Meta:
        model = MenuComposition
        fields = ('recette', 'portions')
        widgets = {
            'recette': autocomplete.ModelSelect2(url='recette-autocomplete'),
        }