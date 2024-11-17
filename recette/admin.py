from django.contrib import admin
from recette.models import Recette, Ingredient, ListeIngredients, Batch, Categorie
from recette.forms import RecetteForm, ListeIngredientForm, BatchForm
# Register your models here.
class ListeIngredientsInline(admin.TabularInline):
    model = ListeIngredients
    form = ListeIngredientForm

class RecetteAdmin(admin.ModelAdmin):
    form = RecetteForm
    inlines = [
        ListeIngredientsInline,
    ]

class BatchAdmin(admin.ModelAdmin):
    model = Batch
    list_display = ['nom','recette','jour']
    form = BatchForm


admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Categorie)