from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from budget.models.depense import Depense
from budget.models.recette import Recette
from budget.models.parametre import Categorie, MoyensPaiement, Origine, Camp


@admin.register(Recette)
class RecetteAdmin(ImportExportModelAdmin):
    list_display = ('intitule', 'montant', 'recu', 'date', 'moyen_paiement', 'origine', 'commentaire')


@admin.register(Depense)
class DepenseAdmin(ImportExportModelAdmin):
    list_display = ('intitule', 'montant', 'categorie', 'date', 'moyen_paiement', 'justificatif', 'justificatifCB', 'commentaire')


@admin.register(Categorie)
class CategorieAdmin(ImportExportModelAdmin):
    pass


@admin.register(MoyensPaiement)
class MoyensPaiementsAdmin(ImportExportModelAdmin):
    pass


@admin.register(Origine)
class OrigineAdmin(ImportExportModelAdmin):
    pass


@admin.register(Camp)
class CampAdmin(ImportExportModelAdmin):
    pass