from django.db import models
from django.utils.formats import date_format

# Create your models here.
class Menu(models.Model):
    date = models.DateField()
    date_fin = models.DateField()
    recettes = models.ManyToManyField('recette.Recette', through='MenuComposition')
    
    def __str__(self):
        return "Menu du {0} au {1}".format(date_format(self.date), date_format(self.date_fin))

class MenuComposition(models.Model):
    recette = models.ForeignKey('recette.Recette', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    portions = models.IntegerField()