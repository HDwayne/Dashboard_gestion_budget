from django.forms import ModelForm

from budget.models.parametre import MoyensPaiement


class MoyensPaiementsForm(ModelForm):
    class Meta:
        model = MoyensPaiement
        fields = ('moyens',)
