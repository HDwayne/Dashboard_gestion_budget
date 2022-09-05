from django.db import models


class MoyensPaiement(models.Model):
    moyens = models.CharField(verbose_name="Moyens de paiements", null=True, blank=True, max_length=40)

    def __str__(self):
        return self.moyens


class Origine(models.Model):
    origine = models.CharField(verbose_name="Origine", null=True, blank=True, max_length=40)

    def __str__(self):
        return self.origine


class Categorie(models.Model):
    categorie = models.CharField(verbose_name="Catégorie", null=True, blank=True, max_length=40)
    montant_previsionnel = models.FloatField(verbose_name="montant prévisionnel", default=0)

    def __str__(self):
        return self.categorie


class Camp(models.Model):
    date_debut = models.DateField(verbose_name="Date de debut du camp")
    date_fin = models.DateField(verbose_name="Date de fin du camp")

    def __str__(self):
        return str(self.date_debut) + " " + str(self.date_fin)
