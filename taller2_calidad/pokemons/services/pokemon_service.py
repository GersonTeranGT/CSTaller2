import requests
from ..models import Pokemon, Type, Ability

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_list(limit: int = 1351) -> list[dict]:
    """traemos la lista paginada de pokemons (name + url)"""
    response = requests.get(f"{BASE_URL}/pokemon/?limit={limit}")
    if response.status_code != 200:
        print(f"Error al obtener la lista de pokemones: {response.status_code}")
        return []
    return response.json()["results"]


def get_pokemon_detail(url: str) -> dict | None:
    """trae el detalle de un pokemon a partir de su url"""
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener el detalle del pokemon: {response.status_code}")
        return None
    return response.json()


def load_pokemons(limit: int = 1351) -> str:
    """carga los pokemones desde la api a la base de datos solo si esta vacia"""
    if Pokemon.objects.count():
        return "Ya existen pokemones cargados"

    lista = get_pokemon_list(limit)
    if not lista:
        return "No se pudo obtener la lista de pokemones"

    for item in lista:
        data = get_pokemon_detail(item["url"])
        if not data:
            continue

        #para extrer solo lo que nos interesa
        image = data["sprites"]["front_default"]
        type_names = [t["type"]["name"] for t in data["types"]]
        ability_names = [a["ability"]["name"] for a in data["abilities"]]

        #crear el pokemon
        pokemon = Pokemon.objects.create(
            name=data["name"],
            height=data["height"],
            weight=data["weight"],
            image=image or "",
        )

        #crear/obtener los tipos y relacionarlos
        for type_name in type_names:
            type_obj, _ = Type.objects.get_or_create(name=type_name)
            pokemon.types.add(type_obj)

        #crear/obtener las habilidades y relacionarlas
        for ability_name in ability_names:
            ability_obj, _ = Ability.objects.get_or_create(name=ability_name)
            pokemon.abilities.add(ability_obj)

    return f"Se cargaron {Pokemon.objects.count()} pokemones"