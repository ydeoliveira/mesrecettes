from dal import autocomplete
from recette.models import Ingredient, Batch

class BatchAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Batch.objects.none()

        qs = Batch.objects.all()

        if self.q:
            qs = qs.filter(nom__istartswith=self.q)

        return qs
    
class IngredientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Ingredient.objects.none()

        qs = Ingredient.objects.all()

        if self.q:
            qs = qs.filter(nom__istartswith=self.q)

        return qs
