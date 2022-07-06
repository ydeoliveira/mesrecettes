from django.shortcuts import render
from django.views.generic import View

from recette.forms import SearchBar
from recette.models import Recette

# Create your views here.
class SearchEngine(View):
    template_name = 'base.html'
    
    def get(self, request, *args, **kwargs):
        form = SearchBar()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SearchBar(data=request.POST)
        if form.is_valid():
            ingredients = request.POST.getlist('ingredients')
            recettes = Recette.objects.filter(ingredients__in=ingredients).distinct()
            return render(request, self.template_name, {'form': form, 'recettes':recettes})
        return render(request, self.template_name, {'form': form})