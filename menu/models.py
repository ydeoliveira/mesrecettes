from django.db import models

# Create your models here.
class Menu(models.Model):
    date = models.DateField()
    date_fin = models.DateField()
    recettes = models.ManyToManyField('recette.Recette', through='MenuComposition')
    
    def __str__(self):
        return "Menu du {0}".format(self.date)

class MenuComposition(models.Model):
    recette = models.ForeignKey('recette.Recette', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    portions = models.IntegerField()