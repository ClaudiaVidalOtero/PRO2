"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC

class Pokemon(ABC):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type):
        """
        Inicializa.
        Parameters:
            name (str):
        """        
        self.name = name
        self.level = level
        self.strenght = strenght
        self.defense = defense
        self.hp = hp
        self.total_hp = total_hp
        self.agility = agility
        self.pokemon_type = pokemon_type



@abstractmethod
def tafdh(self) xx
    

class WaterPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, surge_mode):
            """Inicializa.
            Parameters:
                surge_mode(bool):   
            """
            self.surge_mode = False
            super(WaterPokemon, self).__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)
            
class FirePokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, temperature):
            """Inicializa.
            Parameters:
                temperature(float):
            """
            self.temperature = temperature
            super(FirePokemon, self).__init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type)

class GrassPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, healing):
        """Inicializa.
        Parameters:
        """
        self.healing = healing
        super(GrassPokemon, self).__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)