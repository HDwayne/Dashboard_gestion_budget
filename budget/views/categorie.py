from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from budget.forms.categorie import CategorieForm
from budget.models.parametre import Categorie
from budget.models.depense import Depense


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.add_categories', raise_exception=True), name='dispatch')
class CreateCategories(CreateView, LoginRequiredMixin):
    model = Categorie
    form_class = CategorieForm
    template_name = 'budget/settings/categorie/categorie_form.html'

    def get_success_url(self):
        return reverse_lazy('settings')


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.change_categories', raise_exception=True), name='dispatch')
class UpdateCategories(UpdateView, LoginRequiredMixin):
    model = Categorie
    form_class = CategorieForm
    template_name = 'budget/settings/categorie/categorie_form.html'

    def get_success_url(self):
        return reverse_lazy('settings')


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.delete_categories', raise_exception=True), name='dispatch')
class DeleteCategories(DeleteView, LoginRequiredMixin):
    model = Categorie
    template_name = 'budget/settings/categorie/categorie_confirm_delete.html'

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if len(Depense.objects.filter(categorie=str(self.object))) == 0:
            self.object.delete()
        return HttpResponseRedirect(reverse_lazy('settings'))
