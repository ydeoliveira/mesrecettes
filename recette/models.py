from django.db import models

from recette.managers import RecetteManager
# Create your models here.

class Recette(models.Model):
    # class Categorie(models.TextChoices):
    #     __empty__ = "---------"
    #     ENTREE = 'Entrée', 'Entrée'
    #     PLAT = 'Plat','Plat',
    #     WEEKEND = 'Plat du weekend','Plat du weekend',
    #     VEGE = 'Plat végé','Plat végé',
    #     DESSERT = 'Dessert','Dessert'
    #     BATCH = 'Batch','Batch'
        
    
    nom = models.CharField(max_length=250, unique=True)
    reference = models.ForeignKey('source.Source', on_delete=models.CASCADE)
    source = models.CharField(max_length=200)
    nombre = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredient', through='ListeIngredients')
    #categorie = models.CharField(max_length=100, choices=Categorie.choices)
    categories = models.ManyToManyField('recette.Categorie')
    description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=300, blank=True, null=True)
    is_batch = models.BooleanField()
    
    objects = RecetteManager()
    
    class Meta:
        ordering = ('nom',)
    
    def __str__(self):
        return self.nom

    # def is_batch(self):
    #     if self.categorie == self.Categorie.BATCH :
    #         return True
    #     else :
    #         return False

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
        CM = 'cm', 'centimètres'
        TRANCHE = 'tr', 'tranches'
        
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    recette = models.ForeignKey('Recette', on_delete=models.CASCADE)
    quantite = models.FloatField()
    unite = models.CharField(max_length=50, choices=Unite.choices)
    
class Batch(models.Model):
    class Jours(models.TextChoices):
        LUNDI = 'lundi', 'lundi'
        MARDI = 'mardi', 'mardi'
        MERCREDI = 'mercredi', 'mercredi'
        JEUDI = 'jeudi', 'jeudi'
        VENDREDI = 'vendredi', 'vendredi'

    
    nom = models.CharField(max_length=200, unique=True)
    recette = models.ForeignKey('Recette', on_delete=models.CASCADE)
    jour = models.CharField(max_length=50, choices=Jours.choices)
    
    def __str__(self):
        return self.nom

class Categorie(models.Model):
    
    nom = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nom
