from django.db import models

MOYENS = (
    ('Carte Bancaire', 'carte bancaire'),
    ('Espèces', 'espèces'),
    ('Chèque', 'chèque'),
    ('Virement Bancaire', 'virement bancaire'),
    ('Autre', 'autre'),
)

ORIGINE = (
    ('Dwayne', 'dwayne'),
    ('Elionor', 'elionor'),
    ('Aurélia', 'aurélia'),
    ('Cannelle', 'cannelle'),
    ('Charlotte', 'charlotte'),
    ('Lilian', 'lilian'),
    ('Tim', 'tim'),
    ('Extra-jobs', 'extra-jobs'),
    ('Groupe', 'groupe'),
    ('Autre', 'autre'),
)


class Recette(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    intitule = models.CharField(verbose_name="intitulé de la recette", max_length=50, default="Recette")
    montant = models.FloatField(verbose_name="Montant de la recette en euro", default=0)

    recu = models.BooleanField(verbose_name="valider la réception", default=0)
    date = models.DateField(verbose_name="Date de réception de la recette", null=True, blank=True)
    moyen_paiement = models.CharField(verbose_name="moyen de paiement", null=True, blank=True, max_length=20)
    origine = models.CharField(verbose_name="Origine de la recette",  null=True, blank=True, max_length=20)
    commentaire = models.TextField(verbose_name="Commentaire", max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.intitule
