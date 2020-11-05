from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_menu/', views.lista_menu, name='lista_menu'),
    path('lista_piatti/', views.lista_piatti, name='lista_piatti'),
    path('lista_ingredienti/', views.lista_ingredienti, name='lista_ingredienti'),
    path('lista_ingredienti/ajax_test/', views.test_ajax, name='test_ajax'),
    path('lista_ingredienti/addIngrediente/', views.addIngrediente, name='addIngrediente'),
]