from django.shortcuts import render
from django.views.generic import View

from recette.forms import SearchBar
from recette.models import Recette
from menu.models import Menu, MenuComposition

DEFAULT_PORTION = 5

# Create your views here.
class Ingredient(View):
    template = "produits.html"
    def get(self, request):
        return render(request, self.template, {})

class SearchEngine(View):
    template_name = 'search.html'
    
    def get(self, request, *args, **kwargs):
        form = SearchBar()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SearchBar(data=request.POST)
        if form.is_valid():
            ingredients = request.POST.getlist('ingredients')
            recettes = Recette.objects.all()
            for ing in ingredients :
                recettes = recettes.filter(ingredients=ing)
            return render(request, self.template_name, {'form': form, 'recettes':recettes.distinct()})
        return render(request, self.template_name, {'form': form})
    
class Recettes(View):
    template_name = 'recettes.html'
    
    def get(self, request, *args, **kwargs):
        recettes = Recette.objects.all()
        return render(request, self.template_name, {'recettes':recettes})
    
    def post(self, request, *args, **kwargs):
        recetteid = request.POST.get("recette")
        print(recetteid)
        try :
            recette = Recette.objects.get(id=recetteid)
            m = Menu.objects.all().order_by('-date_fin')[0]
            MenuComposition.objects.create(recette=recette,
                                           menu = m,
                                           portions=DEFAULT_PORTION)
        except Exception as e:
            print(e)
            recettes = Recette.objects.all()
            return render(request, self.template_name, {'recettes':recettes})
        else :
            recettes = Recette.objects.all()
            return render(request, self.template_name, {'recettes':recettes})
        
        