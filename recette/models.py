from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Recette(models.Model):
    class Categorie(models.TextChoices):
        ENTREE = 'Entrée', 'Entrée'
        PLAT = 'Plat','Plat'
        DESSERT = 'Dessert','Dessert'
    
    
    nom = models.CharField(max_length=250, unique=True)
    reference = models.ForeignKey('source.Source', on_delete=models.CASCADE)
    source = models.CharField(max_length=200)
    nombre = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredient', through='ListeIngredients')
    categorie = models.CharField(max_length=100, choices=Categorie.choices)
    description = models.TextField(blank=True, null=True)
    batch = models.ForeignKey('Batch', blank=True, null=True, on_delete=models.CASCADE)
    image = models.URLField(max_length=300, blank=True, null=True)
    
    class Meta:
        ordering = ('nom',)
    
    def __str__(self):
        return self.nom

class Ingredient(models.Model):
    class Rayon(models.TextChoices):
        PRIMEUR = 'FL', 'Fruits et Légumes'
        VIANDE = 'V', 'Viande'
        POISSON = 'P', 'Poisson'
        PAIN = 'P1', 'Pain et Patisseries'
        FRAI = 'F', 'Frais'
        SUREGELE = 'S', 'Surgelé'
        BOISSON = 'B', 'Boisson'
        SALE = 'SA', 'Epicerie salée'
        SUCRE = 'SU', 'Epicerie sucrée'
        
    nom = models.CharField(max_length=150, unique=True)
    rayon = models.CharField(max_length=100, choices=Rayon.choices)
    placard = models.BooleanField("Produit du placard", default=False)
    bio = models.BooleanField("Produit Bio", default=False)
    
    class Meta:
        ordering = ('nom',)
    
    def __str__(self):
        return self.nom
    
class ListeIngredients(models.Model):
    class Unite(models.TextChoices):
        GRAMME = 'g', 'grammes'
        UNITE = 'u', 'unités'
        PIECE = 'p', 'pièces'
        CLITRE = 'cl', 'cl'
        CAS = 'cas', 'CaS'
        CAC = 'cac', 'CaC'
        BOTTE = 'b','bottes'
        VERRE = 'v', 'verres'
        
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    recette = models.ForeignKey('Recette', on_delete=models.CASCADE)
    quantite = models.FloatField()
    unite = models.CharField(max_length=50, choices=Unite.choices)
    
class Batch(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.nom
     