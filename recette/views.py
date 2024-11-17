from django.shortcuts import render
from django.views.generic import View
from django.http.response import Http404
from django.core.paginator import Paginator

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
            categorie = request.POST.get('categorie')
            recettes = Recette.objects.search_form(ingredients, categorie)
            return render(request, self.template_name, {'form': form, 'recettes':recettes.distinct()})
        return render(request, self.template_name, {'form': form})
    
class Recettes(View):
    template_name = 'recettes.html'
    
    def _paginated_values(self, request, recettes, page_number):
        p = Paginator(recettes, 16)
        page_obj = p.get_page(page_number)
        return page_obj
    
    def get(self, request, *args, **kwargs):
        form = SearchBar()
        try :
            recettes = Recette.objects.search_form(request.session.get('ingredients'), request.session.get('categorie'))
            form = SearchBar(data=request.session)
        except Exception as e:
            recettes = Recette.objects.all()
        page_obj = self._paginated_values(request, recettes, request.GET.get("page"))
        return render(request, self.template_name, {'recettes':page_obj,'form':form})
    
    def post(self, request, *args, **kwargs):
        if "filtering" in request.POST :
            form = SearchBar(data=request.POST)
            if form.is_valid():
                ingredients = request.POST.getlist('ingredients')
                categorie = request.POST.get('categorie')
                request.session['ingredients']=ingredients
                request.session['categorie']=categorie
                recettes = Recette.objects.search_form(ingredients, categorie)
                page_obj = self._paginated_values(request, recettes.distinct(), 1)
                return render(request, self.template_name, {'recettes':page_obj,'form':form})
        elif "recette" in request.POST :
            recetteid = request.POST.get("recette")
            portions = request.POST.get("portions")
            if not portions :
                portions = DEFAULT_PORTION
            try :
                recette = Recette.objects.get(id=recetteid)
                m = Menu.objects.all().order_by('-date_fin')[0]
                if m.recettes.filter(id=recette.id).exists() :
                    mc = MenuComposition.objects.get(recette=recette,
                                                   menu = m)
                    mc.portions = mc.portions+int(portions)
                    mc.save()
                else :
                    MenuComposition.objects.create(recette=recette,
                                                   menu = m,
                                                   portions=portions)
            except Exception as e:
                recettes = Recette.objects.search_form(request.session.get('ingredients'), request.session.get('categorie'))
                page_obj = self._paginated_values(request, recettes.distinct(), request.GET.get("page"))
                return render(request, self.template_name, {'recettes':page_obj, 'form':SearchBar(data=request.session)})
            else :
                recettes = Recette.objects.search_form(request.session.get('ingredients'), request.session.get('categorie'))
                page_obj = self._paginated_values(request, recettes.distinct(), request.GET.get("page"))
                return render(request, self.template_name, {'recettes':page_obj, 'form':SearchBar(data=request.session)})
        else :
            raise Http404()

class VueRecette(View):
    template_name = 'recette-view.html'
    def get(self,request, *args, **kwargs):
        try:
            recette = Recette.objects.get(id=kwargs['pk'])
            return render(request, self.template_name, {'recette':recette})
        except :
            return Http404
