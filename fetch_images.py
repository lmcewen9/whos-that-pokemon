import requests
from game import all_pokemon

def main():
    for i, poke in enumerate(all_pokemon):
        with open(f"images/{poke}.png", 'wb') as file:
            file.write(requests.get(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i+1}.png").content)

if __name__ == "__main__":
    main()