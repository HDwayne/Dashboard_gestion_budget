from django.forms import ModelForm, ChoiceField

from budget.models.parametre import MoyensPaiement, Origine
from budget.models.recette import Recette


class RecetteBaseForm:
    def clean(self):
        clean_data = ModelForm.clean(self)

        if not clean_data.get('intitule'):
            msg = "Intitulé doit etre spécifié"
            self._errors['intitule'] = self.error_class([msg])
            del clean_data['intitule']

        if not clean_data.get('montant'):
            msg = "montant doit etre spécifié"
            self._errors['montant'] = self.error_class([msg])
            del clean_data['montant']

        if clean_data.get('recu'):
            if not clean_data.get('date'):
                msg = (
                    "Date de récéption obligatoire car recette noté comme recu"
                )
                self._errors['date'] = self.error_class([msg])
                del clean_data['date']
            if not clean_data.get('moyen_paiement'):
                msg = (
                    "moyen de paiement obligatoire car recette noté comme recu"
                )
                self._errors['moyen_paiement'] = self.error_class([msg])
                del clean_data['moyen_paiement']
            if not clean_data.get('origine'):
                msg = (
                    "origine obligatoire car recette noté comme recu"
                )
                self._errors['origine'] = self.error_class([msg])
                del clean_data['origine']

        return clean_data


class RecetteForm(RecetteBaseForm, ModelForm):
    origine = ChoiceField(choices=[''])
    moyen_paiement = ChoiceField(choices=[''])

    def __init__(self, *args, **kwargs):
        super(RecetteForm, self).__init__(*args, **kwargs)
        self.fields['origine'].choices = [
            (Origine.origine, Origine.origine.lower()) for Origine in Origine.objects.all()
        ]
        self.fields['moyen_paiement'].choices = [
            (MoyensPaiement.moyens, MoyensPaiement.moyens.lower()) for MoyensPaiement in MoyensPaiement.objects.all()
        ]

    class Meta:
        model = Recette
        fields = ('intitule', 'montant', 'recu', 'date', 'moyen_paiement', 'origine', 'commentaire')
