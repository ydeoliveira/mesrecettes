# Generated by Django 3.2 on 2024-11-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0013_remove_recette_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
