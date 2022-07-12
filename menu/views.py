from django.shortcuts import render
from django.views.generic import View

from menu.models import Menu

# Create your views here.
class Courses(View):
    template_name = 'base.html'
    def get(self, request, *args, **kwargs):
        menu = Menu.objects.get(id=kwargs['pk'])
        courses = {}
        for repas in menu.menucomposition_set.all() :
            for ingredient in repas.recette.listeingredients_set.all():
                _rayon = ingredient.ingredient.get_rayon_display()
                _ing = ingredient.ingredient
                _unite = ingredient.unite
                if _rayon not in courses.keys() :
                    courses[_rayon] = {}
                if _ing not in courses[_rayon].keys() :
                    courses[_rayon][_ing] = {}
                if _unite not in courses[_rayon][_ing] :
                    courses[_rayon][_ing][_unite] = 0
                courses[_rayon][_ing][_unite] += ingredient.quantite * repas.portions / ingredient.recette.nombre
        return render(request, self.template_name, {'courses': courses})