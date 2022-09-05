from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from budget.forms.camp import CampForm
from budget.models.parametre import Camp


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.add_camp', raise_exception=True), name='dispatch')
class CreateCamp(CreateView, LoginRequiredMixin):
    model = Camp
    form_class = CampForm
    template_name = 'budget/settings/camp/camp_form.html'

    def get_success_url(self):
        return reverse_lazy('settings')


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('budget.change_camp', raise_exception=True), name='dispatch')
class UpdateCamp(UpdateView, LoginRequiredMixin):
    model = Camp
    form_class = CampForm
    template_name = 'budget/settings/camp/camp_form.html'

    def get_success_url(self):
        return reverse_lazy('settings')
