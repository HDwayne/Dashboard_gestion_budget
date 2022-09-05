from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView

from .models.recette import Recette
from .models.depense import Depense
from .views import dashboard, recette, depense, origine, parametre, moyenspaiement, categorie, camp

urlpatterns = [
    path('', dashboard.index, name='dashboard'),

    path('recettes', recette.recette_list, name='recettes'),
    path('recettes/create', recette.CreateRecette.as_view(), name='create_recette'),
    path('recettes/update/<int:pk>', recette.UpdateRecette.as_view(), name='update_recette'),
    path('recettes/delete/<int:pk>', recette.DeleteRecette.as_view(), name='delete_recette'),
    path('recettes/<int:pk>', login_required(DetailView.as_view(model=Recette,
                                                                template_name='budget/recette/recette_detail.html')),
         name='detail_recette'),

    path('depenses', depense.depense_list, name='depenses'),
    path('depenses/create', depense.CreateDepense.as_view(), name='create_depense'),
    path('depenses/update/<int:pk>', depense.UpdateDepense.as_view(), name='update_depense'),
    path('depenses/delete/<int:pk>', depense.DeleteDepense.as_view(), name='delete_depense'),
    path('depenses/<int:pk>', login_required(DetailView.as_view(model=Depense,
                                                                template_name='budget/depense/depense_detail.html')),
         name='detail_depense'),

    path('settings/', parametre.settings, name='settings'),

    path('settings/origine/create', origine.CreateOrigine.as_view(), name='create_origine'),
    path('settings/origine/delete/<int:pk>', origine.DeleteOrigine.as_view(), name='delete_origine'),

    path('settings/moyenpaiement/create', moyenspaiement.CreateMoyensPaiement.as_view(), name='create_moyenpaiement'),
    path('settings/moyenpaiement/delete/<int:pk>', moyenspaiement.DeleteMoyensPaiement.as_view(),
         name='delete_moyenpaiement'),

    path('settings/categorie/update/<int:pk>', categorie.UpdateCategories.as_view(), name='update_categorie'),
    path('settings/categorie/create', categorie.CreateCategories.as_view(), name='create_categorie'),
    path('settings/categorie/delete/<int:pk>', categorie.DeleteCategories.as_view(), name='delete_categorie'),

    path('settings/camp/update/<int:pk>', camp.UpdateCamp.as_view(), name='update_camp'),
    path('settings/camp/create', camp.CreateCamp.as_view(), name='create_camp'),
]
