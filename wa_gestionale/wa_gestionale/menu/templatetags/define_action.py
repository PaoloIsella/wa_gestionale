from django import template
from datetime import timedelta, datetime

register = template.Library()

@register.simple_tag
def define(val=None):
  return val

@register.simple_tag
def data_fine(data_inizio : datetime, lista_pasti):
  return data_inizio + timedelta(days=len(lista_pasti))

@register.simple_tag
def cambia_stato(stato : bool):
  return not stato