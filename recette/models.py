from django.db import models

# Create your models here.

class Recette(models.Model):
    class Categorie(models.TextChoices):
        ENTREE = 'Entrée', 'Entrée'
        PLAT = 'Plat','Plat'
        DESSERT = 'Dessert','Dessert'
    
    
    nom = models.CharField(max_length=250)
    reference = models.ForeignKey('source.Source', on_delete=models.CASCADE)
    source = models.CharField(max_length=200)
    nombre = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredient', through='ListeIngredients')
    categorie = models.CharField(max_length=100, choices=Categorie.choices)
    description = models.TextField()

class Ingredient(models.Model):
    class Rayon(models.TextChoices):
        PRIMEUR = 'FL', 'Fruits et Légumes'
        VIANDE = 'V', 'Viande'
        POISSON = 'P', 'Poisson'
        PAIN = 'P1', 'Pain et Patisseries'
        FRAI = 'F', 'Frai'
        SUREGELE = 'S', 'Surgelé'
        BOISSON = 'B', 'Boisson'
        SALE = 'SA', 'Epicerie salée'
        SUCRE = 'SU', 'Epicerie sucrée'
        
    name = models.CharField(max_length=150)
    rayon = models.CharField(max_length=100, choices=Rayon.choices)
    
class ListeIngredients(models.Model):
    class Unite(models.TextChoices):
        GRAMME = 'g', 'grammes'
        PIECE = 'p', 'pièces'
        
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    recette = models.ForeignKey('Recette', on_delete=models.CASCADE)
    quantite = models.FloatField()
    unite = models.CharField(max_length=50, choices=Unite.choices)
    
    