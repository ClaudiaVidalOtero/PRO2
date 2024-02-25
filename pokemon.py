"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
class Pokemon(ABC):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type):
        """
        Inicializa.
        Parameters:
            name (str): Nombre del Pokemon.
            level (int): Nivel del Pokemon del 1 hasta al 100.
            strenght (int): Fuerza del Pokemon.
            defense (int): Defensa del Pokemon 
            hp (int): Puntos de salud del Pokemon.
            total_hp (int): Puntos de salud total del Pokemon.
            agility (int): Agilidad del Pokemon.
            pokemon_type (str): Tipo de Pokemon.
        """
        self.name = name
        self.level = level
        self.strenght = strenght
        self.defense = defense
        self.hp = hp
        self.total_hp = total_hp
        self.agility = agility
        self.pokemon_type = pokemon_type

    @property
    def name(self):
        # Property (getter) for the name
        return self.name
    @name.setter
    def name(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value) > 0:
            self.name = value
        else:
            raise ValueError("Name must be a non-empty string")
    @property
    def level(self):
        # Property (getter) for the level
        return self.level
    @level.setter
    def level(self, value: int):
        # Setter for the level
        if isinstance (value, int) and value >= 0:
            self.level = value
        else:
            raise ValueError("Level must be a non-negative integer")

    @property
    def strenght(self):
        # Property (getter) for the strenght
        return self.strenght
    @strenght.setter
    def strenght(self, value: int):
        # Setter for the strenght
        if isinstance (value, int) and value >= 0:
            self.level = value
        else:
            raise ValueError("Strenght must be a non-negative integer")

    @property
    def defense(self):
        # Property (getter) for the defense
        return self.defense    
    @defense.setter
    def defense(self, value: int):
        # Setter for the defense
        if isinstance (value, int) and value >= 0:
            self.defense = value
        else:
            raise ValueError("Defense must be a non-negative integer")
  
    @property
    def hp(self):
        # Property (getter) for the hp
        return self.hp
    @hp.setter
    def hp(self, value: int):
        # Setter for the hp
        if isinstance (value, int) and value >= 0:
            self.defense = value
        else:
            raise ValueError("HP must be a non-negative integer")
    
    @property
    def total_hp(self):
        # Property (getter) for the total hp
        return self.total_hp
    @total_hp.setter
    def name(self, value: int):
        # Setter for the total hp
        if isinstance (value, int) and value >= 0:
            self.total_hp = value
        else:
            raise ValueError("Total HP must be a non-negative integer")
    
    @property
    def agility(self):
        # Property (getter) for the agility
        return self.agility
    @agility.setter
    def agility(self, value: int):
        # Setter for the agility
        if isinstance(value, int) and value >= 0:
            self.agility = value
        else:
            raise ValueError("Agility must be a non-negative integer")

    @property
    def pokemon_type(self):
        # Property (getter) for the pokemon type
        return self.pokemon_type
    @pokemon_type.setter
    def pokemon_type(self, value: str):
        # Setter for the pokemon type
        if isinstance(value, str) and len(value) > 0:
            self.pokemon_type = value
        else:
            raise ValueError("Pokemon type must be a non-empty string")
        
    def basic_attack(self, opponent:'Pokemon') -> int:
        """
        Disminuye el valor del atributo hp del oponente en n unidades de daño, 
        calculadas como el máximo entre 1 y la diferencia entre el atributo strength del atacante y el 
        valor del atributo defense del Pokemon oponente. 
                
        Parameters:
            opponent (Pokemon):

        Returns:
            int: El número de unidades de daño que el Pokemon causó a opponent.
        """
        damage = max(1, (self.strenght - opponent.defense))
        opponent.hp -= damage
        return damage

    def is_debilitated(self) -> bool:
        """
        Indica que el Pokemon está debilitado si los puntos de salud (hp) se encuentra a 0.
        
        Returns:
            bool: True si el atributo hp tiene valor cero, False en caso contrario. 
        """
        return self.hp == 0

    @abstractmethod
    def effectiviness(opponent: 'Pokemon') -> int:
        """
        Descripcion.
        """
        pass  
    def __str__(self) -> str:
        """
        Muestra por pantalla una representación en formato de cadena con información detallada del Pokemon.
        
        Returns:
            str: Una cadena con información detallada del pokemon.
        """

        info = '{name} ({pokemon_type} Stats: )'.format(self.name, self.pokemon_type)
        info += 'Level: {level}, ATT: {strength}, DEF: {defense}, AGI: {agility}, HP: {hp}/{total_hp}.'.format(self.level, self.strength, self.defense, self.agility, self.hp, self.total_hp)
        return info
class WaterPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, surge_mode):
        """
        Inicializa.
        
        Parameters:
            surge_mode(bool):   
        """
        self.surge_mode = surge_mode
        super().__init__(name, level, strenght, defense, hp, total_hp, agility, "Water")

    @property
    def surge_mode(self):
        # Property (getter) for the surge mode
        return self.surge_mode 
    @surge_mode.setter
    def surge_mode(self, value: bool):
        # Setter for the surge mode
        if isinstance(value, bool):
            self.surge_mode = value
        else:
            raise ValueError("Surge mode debe ser un valor booleano.")
        
    def check_surge_activation(self) -> bool:
        """
        Verifica si el modo de aumento debería activarse para un Pokemon si sus puntos de salud es menor que la mitad de los puntos totales de salud. 
        
        Returns:
            bool: True si el atributo hp del Pokemon es inferior a total_hp / 2, y False en caso contrario. 
        """
        return self.hp < self.total_hp/2
    
    def water_attack(self, opponent:'Pokemon') -> int:
        """
        Descripcion.
        Parameters:
            opponent (Pokemon):
        Returns:
            int: El número de unidades de daño causadas. 
        """ 
        self.surge_mode = self.check_surge_activation()
        
        factor_effectiveness = self.effectiveness(opponent)

        if factor_effectiveness == 1:
            factor = 1.5  # Factor correcto para Water contra Fire
        elif factor_effectiveness == 0:
            factor = 1  # Factor correcto para Water contra Water
        elif factor_effectiveness == -1:
            factor = 0.5 # Factor correcto para Water contra Grass
        
        if self.surge_mode: # Ajusta el factor si surge_mode es True
            factor += 0.1

        damage = max(1, round(factor*self.strength) - opponent.defense)
        opponent.hp -= damage
        if opponent.surge_mode:
            factor += 0.1
        return damage

    def effectiveness(opponent: 'Pokemon') -> int:
        """
        Devuelve 1 si el Pokemon es de tipo FirePokemon, 0 si es de tipo WaterPokemon,
        y -1 si es de tipo GrassPokemon.

        Parameters:
        opponent (Pokemon): El Pokemon oponente.
        
        Returns:
            int: Valor de efectividad del ataque en función de los tipos de Pokémon.
        Raises:
            ValueError: No es ningun tipo de Pokemon que tenemos registrado.
        """
        if isinstance(opponent, FirePokemon):
            return 1
        elif isinstance(opponent, WaterPokemon):
            return 0
        elif isinstance(opponent, GrassPokemon):
            return -1
        else:
            raise ValueError("Tipo de Pokemon no reconocido.")
        
class GrassPokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, healing):
        """Inicializa.
        
        Parameters:
            healing (float):
        """
        self.healing = healing
        super().__init__(name, level, strenght, defense, hp, total_hp, agility, "Grass")
    
    @property
    def healing(self):
        # Property (getter) for the healing
        return self.healing 
    @healing.setter
    def healing(self, value: float):
        # Setter for the healing
        if isinstance(value, float) and value > 0:
            self.healing = value
        else:
            raise ValueError("Healing debe ser un valor positivo.")

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
        Devuelve 1 si el Pokemon es de tipo WaterPokemon, 0 si es de tipo GrassPokemon,
        y -1 si es de tipo FirePokemon.

        Parameters:
        opponent (Pokemon): El Pokemon oponente.

        Returns:
            int: Valor de efectividad del ataque en función de los tipos de Pokémon.
        Raises:
            ValueError: No es ningun tipo de Pokemon que tenemos registrado.
        """
        if isinstance(opponent, WaterPokemon):
            return 1
        elif isinstance(opponent, GrassPokemon):
            return 0
        elif isinstance(opponent, FirePokemon):
            return -1
        else:
            raise ValueError("Tipo de Pokemon no reconocido.")
class FirePokemon(Pokemon):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type, temperature):
        """
        Inicializa.
        
        Parameters:
            temperature(float):
        """
        self.temperature = temperature
        super().__init__(self, name, level, strenght, defense, hp, total_hp, agility, "Fire")
    
    @property
    def temperature(self):
        # Property (getter) for the temperature
        return self.temperature 
    @temperature.setter
    def temperature(self, value: float):
        # Setter for the temperature
        if isinstance(value, float) and value > 0:
            self.temperature = value
        else:
            raise ValueError("Temperatura debe ser un valor positivo.")
        
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
        Devuelve 1 si el Pokemon es de tipo GrassPokemon, 0 si es de tipo FirePokemon,
        y -1 si es de tipo WaterPokemon.

        Parameters:
        opponent (Pokemon): El Pokemon oponente.
        
        Returns:
            int: Valor de efectividad del ataque en función de los tipos de Pokémon.
        Raises:
            ValueError: No es ningun tipo de Pokemon que tenemos registrado.
        """
        if isinstance(opponent, GrassPokemon):
            return 1
        elif isinstance(opponent, FirePokemon):
            return 0
        elif isinstance(opponent, WaterPokemon):
            return -1
        else:
            raise ValueError("Tipo de Pokemon no reconocido.")