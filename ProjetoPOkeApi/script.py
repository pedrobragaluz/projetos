import requests as r

pokemons = ["pikachu", "charizard", "bulbasaur", "squirtle"]

for pokemon in pokemons:
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    resposta = r.get(endpoint)

    if resposta.status_code == 200:
        vetor = resposta.json()

    print("Nome do Pokémon: ", vetor['name'])
    print("ID do Pokémon na Pokedex: ", vetor['id'])
else:
    print("Tente outro nome, esse pokémon não existe ")