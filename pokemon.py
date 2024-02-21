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
            strenght (int):
            defense (int)
            hp (int)
            total_hp (int): 
            agility (int):
            pokemon_type (str):
        """      
        self.name = name
        self.level = level
        self.strenght = strenght
        self.defense = defense
        self.hp = hp
        self.total_hp = total_hp
        self.agility = agility
        self.pokemon_type = pokemon_type

    def basic_attack(opponent:'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        pass

    def is_debilitated() -> bool:
        """
        Descripcion.
        
        Returns:
            bool:
        """
        pass

    @abstractmethod
    def effectiviness(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        pass  
    def __str__(self) -> str:
        """ y redefinirá el método mágico __str__() para que al mostrar por pantalla una instancia de un objeto Pokemon 
        devuelva un string con información en el formato:  
                {name} ({pokemon_type}) Stats: Level: {level}, ATT: {strength}, DEF: {defense}, AGI: {agility}, HP: {hp/total_hp}. 
                donde los valores entre {} indican los valores de los atributos del Pokémon.

        Bulbasaur (Grass) Stats: Level: 55, ATT: 67, DEF: 29, AGI: 32, HP: 45/55 
        (donde el 45/55 refleja que el Pokemon ha sufrido 10 puntos de daño respecto a sus puntos de vida totales)."""

        info = '{name} ({pokemon_type} Stats: )'.format(self.get_name(), self.get_pokemon_type())
        info += 'Level: {level}, ATT: {strength}, DEF: {defense}, AGI: {agility}, HP: {hp/total_hp}.'.format(self.get_level(), self.get_strength(), self.get_defense(), self.get_agility())
        return info #COMO SE PONE EL HP?? 

    

class WaterPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, surge_mode):
        """
        Inicializa.
        
        Parameters:
            surge_mode(bool):   
        """
        self.surge_mode = False
        super().__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)
    def water_attack(opponent:'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        pass
    def check_surge_activation() -> bool:
        """
        Descripcion.
        
        Returns:
            bool:
        
        """
        pass
    def effectiveness(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        return super().effectiveness() # lo de super me sale directamente ig pq ya esta en la clase Pokemon
class FirePokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, temperature):
        """
        Inicializa.
        
        Parameters:
            temperature(float):
        """
        self.temperature = temperature
        super().__init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type)
    def fire_attack(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        pass
    def embers(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        pass
    def effectiveness(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        return super().effectiveness()
class GrassPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, healing):
        """Inicializa.
        
        Parameters:
            healing (float):
        """
        self.healing = healing
        super().__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)
    
    def grass_attack(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        pass
    def heal(): 
        """
        Descripcion.
        
        Parameters: 
            None.
        
        Returns:
            int:
        """
        pass
    def effectiveness(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        return super().effectiveness()