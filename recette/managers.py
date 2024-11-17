from django.db import models

class RecetteManager(models.Manager):
    
    def search_form(self, ingredients, categorie):
        recettes = self.all()
        if categorie:
            recettes = recettes.filter(categories=categorie)
        if ingredients :
            for ing in ingredients :
                recettes = recettes.filter(ingredients=ing)
        return recettes