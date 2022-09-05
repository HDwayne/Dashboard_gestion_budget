from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from budget.forms.origine import OrigineForm
from budget.models.parametre import Origine
from budget.models.recette import Recette


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.add_origines', raise_exception=True), name='dispatch')
class CreateOrigine(CreateView, LoginRequiredMixin):
    model = Origine
    form_class = OrigineForm
    template_name = 'budget/settings/origine/origine_form.html'

    def get_success_url(self):
        return reverse_lazy('settings')


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.delete_origines', raise_exception=True), name='dispatch')
class DeleteOrigine(DeleteView, LoginRequiredMixin):
    model = Origine
    template_name = 'budget/settings/origine/origine_confirm_delete.html'

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if len(Recette.objects.filter(origine=str(self.object))) == 0:
            self.object.delete()
        return HttpResponseRedirect(reverse_lazy('settings'))
