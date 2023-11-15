
class OCourses:
    rayons = []
    
    def __init__(self):
        self.rayons = []
    
    def add_rayon(self, rayon):
        self.rayons.append(rayon)
        
    def get_rayons(self):
        return self.rayons
    
    def get_rayon(self, rayon):
        return self.rayons[self.rayons.index(rayon)]
    
    def __str__(self):
        return self.get_rayons()
    
    def __repr__(self):
        return self.get_rayons()

class ORayon:
    ingredients = []
    name = None
    
    def __init__(self, name):
        self.ingredients = []
        self.name = name
    
    def __eq__(self, r):
        return self.name == r.name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def add_ingredient(self, ing):
        self.ingredients.append(ing)
        
    def get_ingredients(self):
        return self.ingredients
    
    def get_ingredient(self, ing):
        return self.ingredients[self.ingredients.index(ing)]

class OIngredient:
    liste = {}
    recettes = []
    name = None
    placard = None
    
    def __init__(self, name, placard):
        self.liste = {}
        self.recettes = []
        self.name = name
        self.placard = placard
        
    def __str__(self):
        return self.name
    
    def __eq__(self, r):
        return self.name == r.name
    
    def __repr__(self):
        return self.name
    
    def set_unit(self, unit):
        self.liste[unit] = 0
    
    def get_units(self):
        return self.liste.keys()
    
    def add_quantite(self, unit, quantite):
        self.liste[unit] += quantite
        
    def add_recette(self, recette):
        self.recettes.append(recette)
    
    def get_recettes(self):
        return self.recettes
    
        