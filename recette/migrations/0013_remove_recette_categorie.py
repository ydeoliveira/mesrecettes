# Generated by Django 3.2 on 2024-11-11 13:58

from django.db import migrations

def migrate_batches(apps, schema_editor):
    Recette = apps.get_model('recette','recette')
    Categorie = apps.get_model('recette','categorie')

    c = Categorie.objects.get(nom='Batch')
    
    for r in Recette.objects.filter(categories=c):
        r.is_batch=True
        r.save()

class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0012_auto_20241111_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recette',
            name='categorie',
        ),
        migrations.RunPython(migrate_batches)
    ]