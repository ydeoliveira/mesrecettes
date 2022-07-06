from django.contrib import admin
from recette.models import Recette, Ingredient, ListeIngredients
from recette.forms import RecetteForm, ListeIngredientForm
# Register your models here.
class ListeIngredientsInline(admin.TabularInline):
    model = ListeIngredients
    form = ListeIngredientForm

class RecetteAdmin(admin.ModelAdmin):
    form = RecetteForm
    inlines = [
        ListeIngredientsInline,
    ]

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient)
#admin.site.register(ListeIngredients)
