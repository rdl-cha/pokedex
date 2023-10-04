import requests
import sys

def search_pokemon(pokedex):
    pokedex = sys.argv[1:]
    for pokemons in pokedex:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemons}/")
        pokemon = response.json()

        # Create empty lists to store attacks and items per pokemon, refreshes every run
        attacks = []
        items = []

        # Get total number of attacks and items and use each total number in while loops to extract each attack and item
        num_attacks = len(pokemon["moves"])
        x = 0
        while x < num_attacks:
            attacks.append(pokemon["moves"][x]["move"]["name"])
            x += 1

        num_items = len(pokemon["held_items"])
        y = 0
        while y < num_items:
            items.append(pokemon["held_items"][y]["item"]["name"])
            y += 1
        
        print("\nName: {}{}\nHP: {}\nBase Experience: {}\nAttacks: {}\nHeld Items: {}\n".format(
            str.upper(pokemon["name"][0]), #Capitalize first letter of name
            pokemon["name"][1:], #the rest of the name
            pokemon["stats"][0]['base_stat'], #kaya 0 kasi yun yung HP na stat
            pokemon["base_experience"],
            (", ").join(attacks), # ", " is the delimiter
            (", ").join(items)
        ))
    

if __name__ == "__main__":
    search_pokemon(sys.argv[1])

# to execute, type:
# python3 pokedex_challenge2.py pokemon1 pokemon2 . . . pokemon6
#change