"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
from pokemon import *

class Trainer: 
    def __init__(self, name, pokemon):
        """
        Inicializa la clase Trainer y se le asignan sus atributos.

        Parameters:
            name (str): Nombre del entrenador.
            pokemon (list): Lista de Pokemons que tiene.
        """
        self.name = name
        self.pokemon = pokemon
    @property
    def name(self):
        # Property (getter) para name
        return self.name
    @name.setter
    def name(self, value):
        # Setter para name
        self.name = value
    @property
    def pokemon(self):
        # Property (getter) para pokemon
        return self.pokemon
    @pokemon.setter
    def pokemon(self, value):
        #Setter para la lista de Pokemon
        self.pokemon = value

    def select_initial_pokemon(self):
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
            Pokemon: next_p, pokemon seleccionado.   
        """
        next_p = None

        for p in self.pokemon: 
            if p.hp > 0:
                if next_p is None or (p.effectiveness(opponent), p.level) > (next_p.effectiveness(opponent), next_p.level):
                    next_p = p
        return next_p
    
    def all_debilitated(self):
        """
        Reconoce si todos los Pokémon del entrenador están debilitados, es decir, los puntos de vida de todos es igual a 0.
        
        Returns:
            bool: True si para todos los Pokémon del entrenador su atributo hp vale cero, False en caso contrario.  
        """
        return all(p.hp == 0 for p in self.pokemon)