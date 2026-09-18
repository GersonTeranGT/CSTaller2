from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Pokemon
from .forms import PokemonForm

# Create your views here.
def pokemon_list(request):
    pokemons_qs = Pokemon.objects.all().order_by('id')
    paginator = Paginator(pokemons_qs, 20)
    page_number = request.GET.get('page')
    pokemons = paginator.get_page(page_number)
    return render(request, "pokemons/pokemon_list.html", {"pokemons": pokemons})


def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, "pokemons/pokemon_detail.html", {"pokemon": pokemon})


def pokemon_create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save()
            return redirect("pokemon_detail", id=pokemon.id)
    else:
        form = PokemonForm()
    return render(request, "pokemons/pokemon_form.html", {"form": form})


def pokemon_update(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            pokemon = form.save()
            return redirect("pokemon_detail", id=pokemon.id)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, "pokemons/pokemon_form.html", {"form": form})

def pokemon_delete(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        pokemon.delete()
        return redirect("pokemon_list")
    return render(request, "pokemons/pokemon_delete.html", {"pokemon": pokemon})