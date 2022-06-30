from django.contrib import admin
from recette.models import Recette, Ingredient, ListeIngredients

# Register your models here.
admin.site.register(Recette)
admin.site.register(Ingredient)
admin.site.register(ListeIngredients)
