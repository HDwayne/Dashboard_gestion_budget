from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from budget.models.parametre import Origine, MoyensPaiement, Categorie, Camp


@login_required()
def settings(request):
    selected = ('Origines', 'MoyensPaiements', 'Categories')
    origine_list = Origine.objects.all()
    moyenpaiement_list = MoyensPaiement.objects.all()
    categorie_list = Categorie.objects.all()
    camp = Camp.objects.first()

    return render(request, 'budget/settings/settings.html', locals())

