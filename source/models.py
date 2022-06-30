from django.db import models
from django.db.models.enums import IntegerChoices

# Create your models here.

class Source(models.Model):
    class SourceType(IntegerChoices):
        LIVRE = 1, "Livre"
        WEB = 2, "Site Web"
        REVUE = 3, "Revue"

    name = models.CharField(max_length=250)
    type = models.IntegerField(choices=SourceType.choices)