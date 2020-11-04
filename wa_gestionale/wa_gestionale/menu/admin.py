from django.contrib import admin
from .models import Ingrediente, Piatto, Menu, IngredientePiatto, PiattoMenu

admin.site.register(Ingrediente)
admin.site.register(Piatto)
admin.site.register(Menu)
admin.site.register(IngredientePiatto)
admin.site.register(PiattoMenu)