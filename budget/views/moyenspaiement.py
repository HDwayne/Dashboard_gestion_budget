from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from budget.forms.moyenpaiement import MoyensPaiementsForm
from budget.models.parametre import MoyensPaiement
from budget.models.depense import Depense
from budget.models.recette import Recette


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.add_moyenspaiements', raise_exception=True), name='dispatch')
class CreateMoyensPaiement(CreateView, LoginRequiredMixin):
    model = MoyensPaiement
    form_class = MoyensPaiementsForm
    template_name = 'budget/settings/moyenspaiement/moyenspaiement_form.html'

    def get_success_url(self):
        return reverse_lazy('settings')


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.delete_moyenspaiements', raise_exception=True), name='dispatch')
class DeleteMoyensPaiement(DeleteView, LoginRequiredMixin):
    model = MoyensPaiement
    template_name = 'budget/settings/moyenspaiement/moyenspaiement_confirm_delete.html'

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if len(Recette.objects.filter(moyen_paiement=str(self.object))) == 0 and\
                len(Depense.objects.filter(moyen_paiement=str(self.object))) == 0:
            self.object.delete()
        return HttpResponseRedirect(reverse_lazy('settings'))
