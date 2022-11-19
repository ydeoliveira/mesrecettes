from django import template

from menu.models import MenuComposition

register = template.Library()

@register.filter
def ratio(recette, menu):
    menu_composition = MenuComposition.objects.get(menu=menu, recette=recette)
    return menu_composition.portions/recette.nombre