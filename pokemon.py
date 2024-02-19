"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
class Pokemon(ABC):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type):
        """
        Inicializa.
        Parameters:
            name (str):
            level (int)
            strenght(int):
            defense(int)
            hp(int)
            total_hp(int): 
            agility(int):
            pokemon_type(str):
        """      
        self.name = name
        self.level = level
        self.strenght = strenght
        self.defense = defense
        self.hp = hp
        self.total_hp = total_hp
        self.agility = agility
        self.pokemon_type = pokemon_type

    def basic_attack(p):
        pass

    def is_debilitated():
        pass

    @abstractmethod
    def effectiveness(p):
         pass  
    

    

class WaterPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, surge_mode):
            """Inicializa.
            Parameters:
                surge_mode(bool):   
            """
            self.surge_mode = False
            super().__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)
            
class FirePokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, temperature):
            """Inicializa.
            Parameters:
                temperature(float):
            """
            self.temperature = temperature
            super().__init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type)

class GrassPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, healing):
        """Inicializa.
        Parameters:
            healing(float):
        """
        self.healing = healing
        super().__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)