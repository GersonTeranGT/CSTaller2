from django.urls import path
from .views import *

urlpatterns = [
    path("", pokemon_list, name="pokemon_list"),
    path("pokemon/<int:id>", pokemon_detail, name="pokemon_detail"),
    path("pokemon/create", pokemon_create, name="pokemon_create"),
    path("pokemon/update/<int:id>", pokemon_update, name="pokemon_update"),
]