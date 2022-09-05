from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

from budget.forms.recette import RecetteForm
from budget.models.parametre import MoyensPaiement, Origine
from budget.models.recette import Recette


@login_required()
@permission_required('budget.view_recette', raise_exception=True)
def recette_list(request):
    selected = 'recette'
    recette_list = Recette.objects.all()

    paginator = Paginator(recette_list.order_by('-date_creation'), 8)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        recette_list = paginator.page(page)
    except EmptyPage:
        recette_list = paginator.page(paginator.num_pages)

    if MoyensPaiement.objects.count() == 0 or Origine.objects.count() == 0:
        can_create = False
    else:
        can_create = True

    return render(request, 'budget/recette/recette_list.html', locals())


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.add_recette', raise_exception=True), name='dispatch')
class CreateRecette(CreateView, LoginRequiredMixin):
    model = Recette
    form_class = RecetteForm
    template_name = 'budget/recette/recette_form.html'

    def get_success_url(self):
        return reverse_lazy('detail_recette', kwargs={"pk": self.object.id})


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.change_recette', raise_exception=True), name='dispatch')
class UpdateRecette(UpdateView, LoginRequiredMixin):
    model = Recette
    form_class = RecetteForm
    template_name = 'budget/recette/recette_form.html'

    def get_success_url(self):
        return reverse_lazy('detail_recette', kwargs={"pk": self.object.id})


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.delete_recette', raise_exception=True), name='dispatch')
class DeleteRecette(DeleteView, LoginRequiredMixin):
    model = Recette
    template_name = 'budget/recette/recette_confirm_delete.html'
    success_url = reverse_lazy('recettes')
