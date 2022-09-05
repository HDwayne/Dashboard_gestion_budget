from django.db import models


def supprime_accent(ligne):
    """ supprime les accents du texte source """
    accents = {'a': ['à', 'ã', 'á', 'â'],
               'e': ['é', 'è', 'ê', 'ë'],
               'i': ['î', 'ï'],
               'u': ['ù', 'ü', 'û'],
               'o': ['ô', 'ö']}
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            ligne = ligne.replace(accented_char, char)
    return ligne


def up_to(instance, filename):
    return '/'.join(['justificatif', supprime_accent(str(instance.intitule)) + '-' + str(instance.montant).replace('.', '_') + '.jpg'])


def cb_up_to(instance, filename):
    return '/'.join(['justificatif_cb', str(instance.intitule) + '-' + str(instance.montant).replace('.', '_') + '.jpg'])


class Depense(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    intitule = models.CharField(verbose_name="intitulé de la recette", max_length=50, default="Dépense")
    categorie = models.CharField(verbose_name="categorie", null=True, blank=True, max_length=30, default='')
    date = models.DateField(verbose_name="Date de la dépense", null=True, blank=True)
    montant = models.FloatField(verbose_name="Montant de la dépense en euro", default=0)
    moyen_paiement = models.CharField(verbose_name="moyen de paiement", null=True, blank=True, max_length=20, default='')
    commentaire = models.TextField(verbose_name="Commentaire - Nom de l'établissement - adresse", max_length=2000,
                                   null=True, blank=True)
    justificatif = models.ImageField(
        verbose_name='justificatif',
        upload_to=up_to,
        null=True,
        blank=True
    )

    justificatifCB = models.ImageField(
        verbose_name='justificatif CB',
        upload_to=cb_up_to,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.intitule
