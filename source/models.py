from django.db import models
from django.db.models.enums import IntegerChoices

# Create your models here.

class Source(models.Model):
    class SourceType(IntegerChoices):
        AUCUNE = 0, "Aucune"
        LIVRE = 1, "Livre"
        WEB = 2, "Site Web"
        REVUE = 3, "Revue"

    nom = models.CharField(max_length=250, unique=True)
    type = models.IntegerField(choices=SourceType.choices)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ('nom',)