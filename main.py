"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import sys
from pokemon import *
from trainer import Trainer
import pandas as pd

class PokemonSimulator:
    """A class that simulates Pokemon trainers and their Pokemon."""

    def create_trainer_and_pokemons(self, text: str):
        """
        Creates a trainer and their pokemons from a given text input.

        Parameters:
        text (str): Multiline text where the first line is the trainer's name and subsequent lines contain Pokemon details.
        
        Returns:
        Trainer instance.
        """

        lines = text.split("\n")
        trainer_name = lines[0]
        pokemons = []

        # Iterating over each pokemon line in the input
        for line in lines[1:]:
            parts = line.split(' (')
            pokemon_name = parts[0] # Extracting the pokemon's name
            details = parts[1].strip(')').split(', ')  # Splitting other attributes
            # Extracting and converting each attribute
            pokemon_type = details[0].split(': ')[1]
            level = int(details[1].split(': ')[1])
            strength = int(details[2].split(': ')[1])
            defense = int(details[3].split(': ')[1])
            hp = int(details[4].split(': ')[1])
            total_hp = hp # Setting total_hp equal to the initial hp
            agility = int(details[5].split(': ')[1])
            
            # Creating pokemons based on their type
            if pokemon_type == 'Fire':
                temperature = details[6].split(': ')[1]
                pokemon_instance = FirePokemon(name=pokemon_name, level=level, strength=strength,
                                               defense=defense, hp=hp, total_hp=total_hp,
                                               agility=agility, pokemon_type=pokemon_type, temperature=temperature)
            elif pokemon_type == 'Grass':
                healing = details[6].split(': ')[1]
                pokemon_instance = GrassPokemon(name=pokemon_name, level=level, strength=strength,
                                                defense=defense, hp=hp, total_hp=total_hp,
                                                agility=agility, pokemon_type=pokemon_type, healing=healing)
            elif pokemon_type == 'Water':
                surge_mode = False
                pokemon_instance = WaterPokemon(name=pokemon_name, level=level, strength=strength,
                                                defense=defense, hp=hp, total_hp=total_hp,
                                                agility=agility, pokemon_type=pokemon_type, surge_mode=surge_mode)
            else: 
                raise ValueError(f"Invalid Pokemon type: {pokemon_type}")
            
            pokemons.append(pokemon_instance)

        # Create an instance of Trainer with the created Pokemon
        trainer_instance = Trainer(name=trainer_name, pokemon=pokemons)

        return trainer_instance

    def parse_file(self, text: str):
        """
        Parses the given text to create trainers and their pokemons.

        Parameters:
        text (str): The full text to be parsed, representing two trainers and their Pokemon.

        Returns:
        None: Currently does not return anything. Intended to return a list of Trainer instances in future development.
        """

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return trainer1, trainer2
    
    def attack(self, round_number, attacker, defender):    
        
        if int(round_number) % 2 != 0:
            type_attack = attacker.pokemon_type.lower() + "_attack"
        else:
            type_attack = "basic_attack"
        
        # Realizar el ataque
        damage = getattr(attacker, type_attack)(defender)
        print(f"-{attacker.name} uses a {type_attack} on {defender.name}! (Damage: -{damage} HP: {defender.hp})")

        # Manejar eventos especiales según el tipo de Pokémon
        if attacker.pokemon_type == "Grass" and round_number % 2 != 0:
            healing = attacker.heal()
            print(f"-{attacker.name} is healing! (Healing: +{healing} HP: {attacker.hp})")
        elif attacker.pokemon_type == "Fire" and round_number % 2 != 0 and not defender.hp <= 0:
            attacker.embers(defender)
            print(f"-{attacker.name} uses embers on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
        
    def print_round_info(self, round_number, p1, p2):
        print(f"┌───────── Round {round_number} ─────────┐")
        print(f"Fighter 1: {p1}")
        print(f"Fighter 2: {p2}")
        print("Actions:") 
    def determine_attack_order(self, pokemon1, pokemon2):
        """
        Determina el orden de ataque basado en la agilidad de los Pokémon.
        """
        if pokemon1.agility >= pokemon2.agility:
            attacker = pokemon1
            defender = pokemon2
        else:
            attacker = pokemon2
            defender = pokemon1

        return attacker, defender
    
    def battle(self, trainer1, trainer2):
        p1 = trainer1.select_first_pokemon()
        p2 = trainer2.select_first_pokemon()

        # Imprimir mensaje indicativo
        print("=================================")
        print(f"Battle between: {trainer1.name} vs {trainer2.name} begins!")
        print(f"{trainer1.name} chooses {p1.name}")
        print(f"{trainer2.name} chooses {p2.name}")
        print("=================================")

        round_number = 1
        no_acabado = True
        while no_acabado:           # Determinar cuál Pokémon ataca primero según la agilidad
            attacker, defender = self.determine_attack_order(p1, p2)
            while not p1.is_debilitated() and not p2.is_debilitated():
                self.print_round_info(round_number, p1, p2)
                self.attack(round_number, attacker, defender)
                self.attack(round_number, defender, attacker)
                round_number += 1

            if p1.is_debilitated():
                selected_pokemon = trainer1.select_next_pokemon(p2)
                if selected_pokemon is not None:
                    print(f"{trainer1.name} chooses {selected_pokemon.name}")
                    p1 = selected_pokemon
                    round_number = 1  # Reiniciar el número de rondas
                else:
                    print("=================================")
                    winner = trainer2
                    print(f"End of the Battle: {winner.name} wins!")
                    print("=================================")
                    # Salir del bucle si no hay más Pokémon disponibles
                    no_acabado = False

            elif p2.is_debilitated():
                selected_pokemon = trainer2.select_next_pokemon(p1)
                if selected_pokemon is not None:
                    print(f"{trainer2.name} chooses {selected_pokemon.name}")
                    p2 = selected_pokemon
                    round_number = 1  # Reiniciar el número de rondas
                else:
                    print("=================================")
                    winner = trainer1
                    print(f"End of the Battle: {winner.name} wins!")
                    print("=================================")
                    # Salir del bucle si no hay más Pokémon disponibles
                    no_acabado = False
        

def main():

    """
    The main function that reads from a file and starts the simulation.
    """

    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)
        simulator.battle(trainer1, trainer2)

if __name__ == '__main__':
    main()
