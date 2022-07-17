# Generated by Django 3.2 on 2022-07-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0003_rename_name_ingredient_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeingredients',
            name='unite',
            field=models.CharField(choices=[('g', 'grammes'), ('p', 'pièces'), ('cl', 'cl')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recette',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]