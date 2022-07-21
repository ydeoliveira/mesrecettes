from django.shortcuts import render
from django.views.generic import View

from recette.forms import SearchBar
from recette.models import Recette

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