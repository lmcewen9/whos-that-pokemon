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
    def __init__(self, pokemon_list:list):
        self.pokemon_list = pokemon_list
        self.game_list = list(self.pokemon_list)
        self.score = 0
        self.question_image = ui.image('').classes('w-64 h-64 object-contain')
        self.option_buttons = []
        self.feedback = ui.label('').style('font-weight: bold; color: green')
        self.score_label = ui.label(f'Score: {self.score}/{len(self.pokemon_list)}')

    def get_random_pokemon(self):
        return self.game_list[random.randint(0, len(self.game_list)-1)]

    def check_answer(self, poke, option):
        if poke == option:
            self.score += 1
            self.feedback.set_text("Correct!")
            self.feedback.style('color: green')
        else:
            self.feedback.set_text(f"Wrong! Answer was: {poke}")
            self.feedback.style('color: red')
        
        self.score_label.set_text(f"Score: {self.score}/{len(self.pokemon_list)}")
        self.show_question()
    
    def get_four_random_pokemon(self, pokemon):
        arr = np.empty(5, dtype='<U10')
        tmp = list(self.pokemon_list)
        arr[random.randint(0,len(arr)-1)] = pokemon
        tmp.remove(pokemon)
        for i in range(len(arr)):
            if arr[i] == '':
                arr[i] = tmp[random.randint(0,len(tmp)-1)]
                tmp.remove(arr[i])
        return arr

    def show_question(self):
        if len(self.game_list) <= 0:
            self.question_image.visible = False
            for btn in self.option_buttons:
                btn.visible = False
            self.feedback.set_text('Quiz Complete!')
            return
        
        poke = self.game_list[random.randint(0,len(self.game_list)-1)]
        self.game_list.remove(poke)
        self.question_image.set_source(f"images/{poke}.png")

        for btn in self.option_buttons:
            btn.delete()
        self.option_buttons.clear()

        for option in self.get_four_random_pokemon(poke):
            btn = ui.button(option, on_click=lambda o=option: self.check_answer(poke, o)).classes('m-1')
            self.option_buttons.append(btn)

@ui.page("/")
def index():
    game = WhosThatPokemon(all_pokemon)
    game.show_question()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Who's that Pokemon!")