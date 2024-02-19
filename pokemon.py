"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC

class Pokemon(ABC):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type):
        
        self.name = name
        self.level = level
        self.strenght = strenght
        self.defense = defense
        self.hp = hp
        self.total_hp = total_hp
        self.agility = agility
        self.pokemon_type = pokemon_type



@abstractmethod
def tafdh(self)
    

class WaterPokemon(Pokemon):
    def __init__(self):
            """Inicializa.
            Parameters:
                None
            """
            super(WaterPokemon, self).__init__()
            
class FirePokemon(Pokemon):
    def __init__(self):
            """Inicializa.
            Parameters:
                None
            """
            super(FirePokemon, self).__init__()

class GrassPokemon(Pokemon):
    def __init__(self):
        """Inicializa.
        Parameters:
            None
        """
        super(GrassPokemon, self).__init__()