# Generated by Django 5.0.6 on 2024-05-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capacite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomEquipement', models.CharField(max_length=100)),
                ('Ram', models.CharField(max_length=100)),
                ('Processeur', models.CharField(max_length=100)),
                ('Stockage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NatureEquipement', models.CharField(max_length=100)),
                ('NomEquipement', models.CharField(max_length=100)),
                ('Marque', models.CharField(max_length=100)),
                ('Service', models.CharField(max_length=100)),
                ('Emplacement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomEquipement', models.CharField(max_length=100)),
                ('SystemeExploitation', models.CharField(max_length=100)),
                ('Logiciel', models.CharField(max_length=100)),
            ],
        ),
    ]