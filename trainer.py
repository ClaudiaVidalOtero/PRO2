"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
from pokemon import *

class Trainer: 
    def __init__(self, name,  pokemon: list[Pokemon]):
        """
        Inicializa la clase Trainer y se le asignan sus atributos.

        Parameters:
            name (str): Nombre del entrenador.
            pokemon (list): Lista de Pokemons que tiene.
        """
        self._name = name
        self._pokemon = pokemon
    @property
    def name(self):
        # Property (getter) para name
        return self._name

    @property
    def pokemon(self):
        # Property (getter) para pokemon
        return self._pokemon
    @pokemon.setter
    def pokemon(self, value):
        #Setter para la lista de Pokemon
        self._pokemon = value

    def select_first_pokemon(self):
        """
        Selecciona el primer pokemon no debilitado.

        Returns:
            Pokemon: p, pokemon seleccionado.
            None: No devuelve nada si no le quedan pokemons o están todos debilitados.
        """
        for p in self.pokemon:
            if p.hp > 0:
                return p
        return None

    def select_next_pokemon(self, opponent):
        """
        Selecciona el Pokemon no debilitado del Entrenador que mejor pueda hacer frente al Pokemon oponente.

        Parameters: 
            opponent: Pokemon oponente
        Returns:
            Pokemon: next_pokemon, pokemon seleccionado.   
        """
        next_pokemon = None
        for p in self.pokemon: 
            if not p.is_debilitated():
                if next_pokemon is None or (p.effectiveness(opponent), p.level) > (next_pokemon.effectiveness(opponent), next_pokemon.level):
                    next_pokemon = p
        return next_pokemon
    
    
    def all_debilitated(self):
        """
        Reconoce si todos los Pokémon del entrenador están debilitados, es decir, los puntos de vida de todos es igual a 0.
        
        Returns:
            bool: True si para todos los Pokémon del entrenador su atributo hp vale cero, False en caso contrario.  
        """
        return all(p.hp == 0 for p in self.pokemon)