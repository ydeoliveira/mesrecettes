from dal import autocomplete
from recette.models import Ingredient, Batch, Recette, Categorie

class BatchAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Batch.objects.none()

        qs = Batch.objects.all()

        if self.q:
            qs = qs.filter(nom__contains=self.q)

        return qs
    
class IngredientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Ingredient.objects.none()

        qs = Ingredient.objects.all()

        if self.q:
            qs = qs.filter(nom__contains=self.q)

        return qs
    
class RecetteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Ingredient.objects.none()

        qs = Recette.objects.all()

        if self.q:
            qs = qs.filter(nom__contains=self.q)

        return qs

class CategorieAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Ingredient.objects.none()

        qs = Categorie.objects.all()

        if self.q:
            qs = qs.filter(nom__contains=self.q)

        return qs