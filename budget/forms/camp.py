from django.forms import ModelForm

from budget.models.parametre import Camp


class CampBaseForm:
    def clean(self):
        clean_data = ModelForm.clean(self)

        def verifier_element(name):
            if not clean_data.get(name):
                msg = f"{name} doit être spécifié"
                self._errors[name] = self.error_class([msg])
                del clean_data[name]


        verifier_element('date_debut')
        verifier_element('date_fin')

        return clean_data


class CampForm(CampBaseForm, ModelForm):
    class Meta:
        model = Camp
        fields = ('date_debut', 'date_fin')
