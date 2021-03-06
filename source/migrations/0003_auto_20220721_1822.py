# Generated by Django 3.2 on 2022-07-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0002_rename_name_source_nom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ('nom',)},
        ),
        migrations.AlterField(
            model_name='source',
            name='nom',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='type',
            field=models.IntegerField(choices=[(0, 'Aucune'), (1, 'Livre'), (2, 'Site Web'), (3, 'Revue')]),
        ),
    ]
