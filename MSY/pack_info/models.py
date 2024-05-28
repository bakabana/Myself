from django.db import models

class Utilisateur(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    est_connecte = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Equipement(models.Model):
    NatureEquipement = models.CharField(max_length=100)
    NomEquipement = models.CharField(max_length=100)
    Marque = models.CharField(max_length=100)
    Service = models.CharField(max_length=100)
    Emplacement = models.CharField(max_length=100)

class Software(models.Model):
    NomEquipement = models.CharField(max_length=100)
    SystemeExploitation = models.CharField(max_length=100)
    Logiciel = models.CharField(max_length=100)

class Capacite(models.Model):
    NomEquipement = models.CharField(max_length=100)
    Ram = models.CharField(max_length=100)
    Processeur = models.CharField(max_length=100)
    Stockage = models.CharField(max_length=100)


# Create your models here.
