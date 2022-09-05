from django.forms import ModelForm

from budget.models.parametre import Origine


class OrigineForm(ModelForm):
    class Meta:
        model = Origine
        fields = ('origine',)
