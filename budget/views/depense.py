from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

from budget.forms.depense import DepenseForm
from budget.models.parametre import MoyensPaiement
from budget.models.parametre import Categorie
from budget.models.depense import Depense


@login_required()
@permission_required('budget.view_depense', raise_exception=True)
def depense_list(request):
    selected = 'depense'
    depense_list = Depense.objects.all()

    paginator = Paginator(depense_list.order_by('-date_creation'), 8)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        depense_list = paginator.page(page)
    except EmptyPage:
        depense_list = paginator.page(paginator.num_pages)

    if MoyensPaiement.objects.count() == 0 or Categorie.objects.count() == 0:
        can_create = False
    else:
        can_create = True

    return render(request, 'budget/depense/depense_list.html', locals())


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.add_depense', raise_exception=True), name='dispatch')
class CreateDepense(CreateView, LoginRequiredMixin):
    model = Depense
    form_class = DepenseForm
    template_name = 'budget/depense/depense_form.html'

    def get_success_url(self):
        return reverse_lazy('detail_depense', kwargs={"pk": self.object.id})


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.change_depense', raise_exception=True), name='dispatch')
class UpdateDepense(UpdateView, LoginRequiredMixin):
    model = Depense
    form_class = DepenseForm
    template_name = 'budget/depense/depense_form.html'

    def get_success_url(self):
        return reverse_lazy('detail_depense', kwargs={"pk": self.object.id})


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.delete_depense', raise_exception=True), name='dispatch')
class DeleteDepense(DeleteView, LoginRequiredMixin):
    model = Depense
    template_name = 'budget/depense/depense_confirm_delete.html'
    success_url = reverse_lazy('depenses')

