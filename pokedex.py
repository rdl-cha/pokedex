import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()
    print("Name: {}{}\nID: {}\nBase XP: {}".format(
        str.upper(pokemon["name"][0]),
        pokemon["name"][1:],
        pokemon["id"],
        pokemon["base_experience"]
    ))

if __name__ == "__main__":
    search_pokemon(sys.argv[1])