from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingrediente(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    unita_misura = models.CharField(max_length=16)
    euro_kg = models.FloatField()
    data_inserimento = models.DateTimeField(auto_now_add=True, auto_now=False)
    colore = models.CharField(max_length=8, blank=True)
    note = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.nome



class Piatto(models.Model):
    class FasciPrezzo(models.TextChoices):
        BASSO = 'B', _('Basso')
        MEDIO = 'M', _('Medio')
        ALTO  = 'A', _('Alto')
    nome = models.CharField(max_length=32, unique=True)
    url_ricetta = models.URLField(blank=True)
    fascia_prezzo = models.CharField(
        max_length=1,
        choices=FasciPrezzo.choices)
    data_inserimento = models.DateTimeField(auto_now_add=True, auto_now=False)
    colore = models.CharField(max_length=8, blank=True)
    note = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.nome



class Menu(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    data_inizio = models.DateField(auto_now_add=False, auto_now=False)
    data_inserimento = models.DateTimeField(auto_now_add=True, auto_now=False)
    colore = models.CharField(max_length=8, blank=True)
    note = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.nome

class IngredientePiatto(models.Model):
    id_ingrediente_piatto = models.BigAutoField(primary_key=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    piatto = models.ForeignKey(Piatto, on_delete=models.CASCADE)
    quantita = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ingrediente', 'piatto'], name='unique_ingrediente_piatto')
        ]

    def __str__(self):
        return f"{self.ingrediente.nome} - {self.piatto.nome}"




class PiattoMenu(models.Model):
    class PranzoCena(models.TextChoices):
        PRANZO = 'P', _('Pranzo')
        CENA = 'C', _('Cena')
    id_piatto_menu = models.BigAutoField(primary_key=True)
    piatto = models.ForeignKey(Piatto, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    data_pasto = models.DateField(auto_now=False, auto_now_add=False)
    pranzo_cena = models.CharField(
        max_length=1,
        choices=PranzoCena.choices,
        blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['piatto', 'menu', 'data_pasto', 'pranzo_cena'], name='unique_piatto_menu')
        ]

    def __str__(self):
        return f"{self.menu.nome} - {self.pranzo_cena}"