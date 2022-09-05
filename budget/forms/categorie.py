from django.forms import ModelForm

from budget.models.parametre import Categorie


class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ('categorie', 'montant_previsionnel')
