import datetime

from django.shortcuts import render
from django.views.generic import View

from menu.models import Menu

# Create your views here.

class MenuList(View):
    template_name = "menus.html"
    def get(self, request):
        menus = Menu.objects.all().order_by('-date')
        return render(request, self.template_name, {'menus': menus,})
    
class Courses(View):
    template_name = "courses.html"
    def get(self, request, *args, **kwargs):
        menu = Menu.objects.get(id=kwargs['pk'])
        courses = {}
        placard = set()
        repas = {}
        tags = "abcdefghijklmnopqrstuvwxyz"
        i=0
        for plat in menu.menucomposition_set.all() :
            repas[tags[i]] = plat
            for ingredient in plat.recette.listeingredients_set.all():
                _rayon = ingredient.ingredient.get_rayon_display()
                _ing = ingredient.ingredient
                _unite = ingredient.unite
                if _rayon not in courses.keys() :
                    courses[_rayon] = {}
                if _ing not in courses[_rayon].keys() and _ing.placard == False :
                    courses[_rayon][_ing] = {}
                elif _ing.placard == True :
                    placard.add(_ing)
                if _ing.placard == False and _unite not in courses[_rayon][_ing] :
                    courses[_rayon][_ing][_unite] = 0
                if _ing.placard == False and "0repas" not in courses[_rayon][_ing] :
                    courses[_rayon][_ing]["0repas"] = []
                if _ing.placard == False :
                    courses[_rayon][_ing][_unite] += ingredient.quantite * plat.portions / ingredient.recette.nombre
                    courses[_rayon][_ing]["0repas"].append(tags[i])
            i+=1
        mode = request.GET.get("mode")
        
        if mode and mode=="print" :
            return render(request, "courses-nocss.html", {'courses': courses, 'placard':placard, 'menu':menu, 'repas':repas})
        else :
            return render(request, self.template_name, {'courses': courses, 'placard':placard, 'menu':menu, 'repas':repas})

class GridMenu(View):
    template_name = "grid.html"
    def get(self, request, *args, **kwargs):
        menu = Menu.objects.get(id=kwargs['pk'])
        date_range = [menu.date + datetime.timedelta(days=x) for x in range((menu.date_fin-menu.date).days+1)]
        print(date_range)
        return render(request, self.template_name, {'menu':menu, 'dates':date_range, 'weekdays':list(range(7,1000,7)), 'sevendays':list(range(0,7)) })
