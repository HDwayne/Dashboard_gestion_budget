from django.forms import ModelForm, ChoiceField

from budget.models.parametre import Categorie, MoyensPaiement
from budget.models.depense import Depense


class DepenseBaseForm:
    def clean(self):
        clean_data = ModelForm.clean(self)

        def verifier_element(name):
            if not clean_data.get(name):
                msg = f"{name} doit être spécifié"
                self._errors[name] = self.error_class([msg])
                del clean_data[name]

        verifier_element('intitule')
        verifier_element('montant')
        verifier_element('categorie')
        verifier_element('date')
        verifier_element('moyen_paiement')

        return clean_data


class DepenseForm(DepenseBaseForm, ModelForm):
    categorie = ChoiceField(choices=[''])
    moyen_paiement = ChoiceField(choices=[''])

    def __init__(self, *args, **kwargs):
        super(DepenseForm, self).__init__(*args, **kwargs)
        self.fields['categorie'].choices = [
            (Categorie.categorie, Categorie.categorie.lower()) for Categorie in Categorie.objects.all()
        ]
        self.fields['moyen_paiement'].choices = [
            (MoyensPaiement.moyens, MoyensPaiement.moyens.lower()) for MoyensPaiement in MoyensPaiement.objects.all()
        ]

    class Meta:
        model = Depense
        fields = ('intitule', 'montant', 'categorie', 'date', 'moyen_paiement', 'justificatif', 'justificatifCB', 'commentaire')
