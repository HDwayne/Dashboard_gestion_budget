from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from budget.models.parametre import Categorie, Camp
from budget.models.depense import Depense
from budget.models.recette import Recette
from datetime import datetime, timedelta


@login_required
def index(request):
    class InfoCategorie:
        def __init__(self, name, pourcentage, montant_actuel, montant_previsionnel):
            self.name = name
            self.pourcentage = pourcentage
            self.montant_actuel = montant_actuel
            self.montant_previsionnel = montant_previsionnel

    depenses = Depense.objects.all()
    recettes = Recette.objects.all()
    categorie = Categorie.objects.all()

    tt_depenses = float()
    for item in depenses:
        tt_depenses += item.montant

    tt_recettes = float()
    tt_recettes_dispo = float()
    for item in recettes:
        if item.recu:
            tt_recettes_dispo += item.montant
        tt_recettes += item.montant

    info_categorie = []
    for cate in categorie:
        montant_actuel = sum([item.montant for item in Depense.objects.all().filter(categorie=cate.categorie)])
        montant_previsionnel = cate.montant_previsionnel
        name = cate.categorie
        try:
            pourcentage = int((montant_actuel / montant_previsionnel) * 100)
        except ZeroDivisionError:
            pourcentage = 0
        info_categorie.append(InfoCategorie(name=name, pourcentage=pourcentage, montant_actuel=montant_actuel,
                                            montant_previsionnel=montant_previsionnel))

    montant_restant_liquide = sum([item.montant for item in Recette.objects.filter(moyen_paiement='Espèces')]) - sum(
        [item.montant for item in Depense.objects.filter(moyen_paiement='Espèces')])
    montant_restant_liquide_disponible = sum(
        [item.montant for item in Recette.objects.filter(moyen_paiement='Espèces', recu=True)]) - sum(
        [item.montant for item in Depense.objects.filter(moyen_paiement='Espèces')])
    montant_restant_cb = sum([item.montant for item in Recette.objects.filter(moyen_paiement='Carte Bancaire')]) - sum(
        [item.montant for item in Depense.objects.filter(moyen_paiement='Carte Bancaire')])
    montant_restant_cb_disponible = sum(
        [item.montant for item in Recette.objects.filter(moyen_paiement='Carte Bancaire', recu=True)]) - sum(
        [item.montant for item in Depense.objects.filter(moyen_paiement='Carte Bancaire')])

    recettes_restant = tt_recettes - tt_depenses
    recettes_restant_dispo = tt_recettes_dispo - tt_depenses

    context = {
        "last_Depenses": Depense.objects.all()[:6:-1],
        "Info_categorie": info_categorie,

        "TT_Recettes": tt_recettes,
        "TT_Depenses": tt_depenses,
        "Recettes_restant": recettes_restant,

        "TT_Recettes_dispo": tt_recettes_dispo,
        "Recettes_restant_dispo": recettes_restant_dispo,

        "montant_restant_liquide": montant_restant_liquide,
        "montant_restant_liquide_disponible": montant_restant_liquide_disponible,

        "montant_restant_cb": montant_restant_cb,
        "montant_restant_cb_disponible": montant_restant_cb_disponible,
    }

    if Camp.objects.first():
        context["camp_config"] = True
        context["camp_end"] = False
        if Camp.objects.first().date_debut > datetime.now().date():
            context["camp_start"] = False
            context["jours_restant_depart"] = (Camp.objects.first().date_debut - datetime.now().date()).days
        else:
            jours_restant = (Camp.objects.first().date_fin - datetime.now().date()).days
            if jours_restant >= 1:
                montant_jour_th = recettes_restant / jours_restant
                montant_jour = recettes_restant_dispo / jours_restant

                context["montant_jour"] = montant_jour
                context["montant_jour_th"] = montant_jour_th
                context["jours_restant"] = jours_restant
                context["camp_start"] = True
            else:
                context["camp_end"] = True

    else:
        context["camp_config"] = False

    return render(request, 'budget/dashboard.html', context)
