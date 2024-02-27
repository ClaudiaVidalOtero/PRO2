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
        # Property (getter) para name
        return self.name
    @name.setter
    def name(self, value: str):
        # Setter para name
        if isinstance(value, str) and len(value) > 0:
            self.name = value
        else:
            raise ValueError("Name must be a non-empty string")
    @property
    def level(self):
        # Property (getter) para level
        return self.level
    @level.setter
    def level(self, value: int):
        # Setter para level
        if isinstance (value, int) and value >= 0:
            self.level = value
        else:
            raise ValueError("Level must be a non-negative integer")

    @property
    def strenght(self):
        # Property (getter) para strenght
        return self.strenght
    @strenght.setter
    def strenght(self, value: int):
        # Setter para strenght
        if isinstance (value, int) and value >= 0:
            self.level = value
        else:
            raise ValueError("Strenght must be a non-negative integer")

    @property
    def defense(self):
        # Property (getter) para defense
        return self.defense    
    @defense.setter
    def defense(self, value: int):
        # Setter para defense
        if isinstance (value, int) and value >= 0:
            self.defense = value
        else:
            raise ValueError("Defense must be a non-negative integer")
  
    @property
    def hp(self):
        # Property (getter) para hp
        return self.hp
    @hp.setter
    def hp(self, value: int):
        # Setter para hp
        if isinstance (value, int) and value >= 0:
            self.defense = value
        else:
            raise ValueError("HP must be a non-negative integer")
    
    @property
    def total_hp(self):
        # Property (getter) para total hp
        return self.total_hp
    @total_hp.setter
    def name(self, value: int):
        # Setter para total hp
        if isinstance (value, int) and value >= 0:
            self.total_hp = value
        else:
            raise ValueError("Total HP must be a non-negative integer")
    
    @property
    def agility(self):
        # Property (getter) para agility
        return self.agility
    @agility.setter
    def agility(self, value: int):
        # Setter para agility
        if isinstance(value, int) and value >= 0:
            self.agility = value
        else:
            raise ValueError("Agility must be a non-negative integer")

    @property
    def pokemon_type(self):
        # Property (getter) para pokemon type
        return self.pokemon_type
    @pokemon_type.setter
    def pokemon_type(self, value: str):
        # Setter para pokemon type
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
        super().__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)

    @property
    def surge_mode(self):
        # Property (getter) para surge mode
        return self.surge_mode 
    @surge_mode.setter
    def surge_mode(self, value: bool):
        # Setter para surge mode
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

        if isinstance(opponent, FirePokemon):
            factor = 1.5
        elif isinstance(opponent, WaterPokemon):
            factor = 1
        elif isinstance(opponent, GrassPokemon):
            factor = 0.5
        else:
            raise ValueError("Tipo de Pokemon no reconocido.")
        
        if self.surge_mode: # Ajusta el factor si surge_mode es True
            factor += 0.1

        damage = max(1, round(factor*self.strength) - opponent.defense)
        opponent.hp -= damage

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
        """Inicializa el Pokemon tipo Grass
        
        Parameters:
            healing (float):
        """
        self.healing = healing
        super().__init__(name, level, strenght, defense, hp, total_hp, agility, pokemon_type)
    
    @property
    def healing(self):
        # Property (getter) para healing
        return self.healing 
    @healing.setter
    def healing(self, value: float):
        # Setter para healing
        if isinstance(value, float) and value > 0:
            self.healing = value
        else:
            raise ValueError("Healing debe ser un valor positivo.")

    def grass_attack(self, opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int: El número de unidades de daño causadas. 
        """

        if isinstance(opponent, WaterPokemon):
            factor = 1.5
        elif isinstance(opponent, GrassPokemon):
            factor = 1
        elif isinstance(opponent, FirePokemon):
            factor = 0.5
        else:
            raise ValueError("Tipo de Pokemon no reconocido.")
    
        damage = max(1, round(factor*self.strength) - opponent.defense)
        opponent.hp -= damage

        return damage
    
    def heal(self) -> int: 
        """
        Descripcion.
        
        Returns:
            int: El número de unidades de puntos de vida efectivas en las que se ha curado el objetivo.
        """
        heal_points = round(self.healing * self.hp)
        healed_hp = heal_points + self.hp

        if healed_hp > self.total_hp:
            heal_points = self.total_hp - self.hp
            self.hp = self.total_hp
            return heal_points
        elif healed_hp <= self.total_hp:
            self.hp = healed_hp
            return heal_points

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
        super().__init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type)
    
    @property
    def temperature(self):
        # Property (getter) para temperature
        return self.temperature 
    @temperature.setter
    def temperature(self, value: float):
        # Setter para temperature
        if isinstance(value, float) and value > 0:
            self.temperature = value
        else:
            raise ValueError("Temperatura debe ser un valor positivo.")
        
    def fire_attack(self, opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int: El número de unidades de daño causadas. 
        """
        if isinstance(opponent, GrassPokemon):
            factor = 1.5
        elif isinstance(opponent, FirePokemon):
            factor = 1
        elif isinstance(opponent, WaterPokemon):
            factor = 0.5
        else:
            raise ValueError("Tipo de Pokemon no reconocido.")

        damage = max(1, round(factor*self.strength) - opponent.defense)
        opponent.hp -= damage

        return damage
    def embers(self, opponent: 'Pokemon') -> int:
        """
        Descripcion.
        
        Parameters:
            opponent ():

        Returns:
            int:
        """
        damage = self.strenght*self.temperature
        opponent.hp -= damage
        return damage
    
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