import requests
import random
import numpy as np
from nicegui import ui, app

all_pokemon = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat",
    "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck",
    "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag",
    "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
    "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch’d", "Doduo",
    "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
    "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee",
    "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute",
    "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung",
    "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela",
    "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu",
    "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar",
    "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto",
    "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
    "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno",
    "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo",
    "Mew"
]

app.add_static_files("images", "images")

class WhosThatPokemon():
    def __init__(self, pokemon_list):
        self.pokemon_list = pokemon_list
        self.current_question_index = 0
        self.score = 0
        self.question_image = ui.image('').classes('w-64 h-64 object-contain')
        self.question_text = ui.label('')
        self.option_buttons = []
        self.feedback = ui.label('').style('font-weight: bold; color: green')
        self.score_label = ui.label(f'Score: {self.score}/{len(self.pokemon_list)}')
        self.next_button = ui.button('Next', on_click=lambda: self.show_question()).props('disabled')
    
    def get_score(self):
        return self.score

    def get_random_pokemon(self):
        return self.game_list[random.randint(0, len(self.game_list)-1)]
    
    def get_four_random_pokemon(self, pokemon):
        arr = np.empty(5, dtype='<U10')
        tmp = self.pokemon_list
        arr[random.randint(0,len(arr)-1)] = pokemon
        tmp.remove(pokemon)
        for i in range(len(arr)):
            if arr[i] == '':
                arr[i] = tmp[random.randint(0,len(tmp)-1)]
                tmp.remove(arr[i])
        return arr

    def show_question(self):
        if self.current_question_index >= len(self.pokemon_list):
            self.question_image.visible = False
            for btn in self.option_buttons:
                btn.visible = False
            self.feedback.set_text('Quiz Complete!')
            self.next_button.disable()
            return
        
        q = self.pokemon_list[self.current_question_index]
        self.question_image.set_source(f"images/{q}.png")


def download_images():
    for i, poke in enumerate(all_pokemon):
        with open(f"images/{poke}.png", 'wb') as file:
            file.write(requests.get(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i+1}.png").content)

@ui.page("/")
def index():
    ui.label('Welcome to my NiceGUI app!')
    ui.button('Click me', on_click=lambda: ui.notify('Button clicked!'))

def main():
    #download_images()
    game = WhosThatPokemon(all_pokemon)
    poke = game.get_random_pokemon()
    print(poke)
    print(game.get_four_random_pokemon(poke))

if __name__ in {"__main__", "__mp_main__"}:
    #ui.run(title="Who's that Pokemon!")
    main()