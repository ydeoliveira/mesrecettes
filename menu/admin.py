from django.contrib import admin
from .models import Menu, MenuComposition
from .forms import MenuCompositionForm

# Register your models here.
class MenuCompositionInline(admin.TabularInline):
    model = MenuComposition
    form = MenuCompositionForm

class MenuAdmin(admin.ModelAdmin):
    model = Menu
    inlines = [
        MenuCompositionInline,
    ]
    
admin.site.register(Menu, MenuAdmin)