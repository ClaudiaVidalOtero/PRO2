"""
TODO: Implement in this file the Pokemon hierarchy.
"""
from abc import ABC, abstractmethod
class Pokemon(ABC):
    def __init__(self, name, level, strenght, defense, hp, total_hp, agility, pokemon_type):
        """
        Inicializa la clase Pokemon y se le asignan sus atributos.

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
    def name(self, value):
        # Setter para name
        self.name = value

    @property
    def level(self):
        # Property (getter) para level
        return self.level
    @level.setter
    def level(self, value):
        # Setter para level
        self.level = value

    @property
    def strenght(self):
        # Property (getter) para strenght
        return self.strenght
    @strenght.setter
    def strenght(self, value):
        # Setter para strenght
        self.strenght = value

    @property
    def defense(self):
        # Property (getter) para defense
        return self.defense    
    @defense.setter
    def defense(self, value):
        # Setter para defense
        self.defense = value
  
    @property
    def hp(self):
        # Property (getter) para hp
        return self.hp
    @hp.setter
    def hp(self, value):
        # Setter para hp
        if value >= 0:
            self.hp = value
        else:
            self.hp = 0
    
    @property
    def total_hp(self):
        # Property (getter) para total hp
        return self.total_hp
    @total_hp.setter
    def total_hp(self, value):
        # Setter para total hp
        self.total_hp = value

    @property
    def agility(self):
        # Property (getter) para agility
        return self.agility
    @agility.setter
    def agility(self, value):
        # Setter para agility
        self.agility = value

    @property
    def pokemon_type(self):
        # Property (getter) para pokemon type
        return self.pokemon_type
    @pokemon_type.setter
    def pokemon_type(self, value):
        # Setter para pokemon type
        self.pokemon_type = value
    
    def basic_attack(self, opponent:'Pokemon') -> int:
        """
        Disminuye el valor del atributo hp del oponente ens n unidades de daño.
                
        Parameters:
            opponent (Pokemon): El Pokemon oponente.

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
    def effectiviness(self, opponent: 'Pokemon') -> int:
        """
        Método abstracto que heredan las subclases de pokemon.
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
        Inicializa la subclase WaterPokemon, hereda los atributos de Pokemon y se le asigna un atributo más propio.
        
        Parameters:
            surge_mode(bool): Modo de aumento del pokemon.
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
        self.surge_mode = value
        
    def check_surge_activation(self) -> bool:
        """
        Verifica si el modo de aumento debería activarse para un Pokemon si sus puntos de salud es menor que la mitad de los puntos totales de salud. 
        
        Returns:
            bool: True si el atributo hp del Pokemon es inferior a total_hp / 2, y False en caso contrario. 
        """
        return self.hp < self.total_hp/2
    
    def water_attack(self, opponent:'Pokemon') -> int:
        """
        Disminuye la vida del oponente en n unidades de daño.

        Parameters:
            opponent (Pokemon): El Pokemon oponente.
        Returns:
            int: El número de unidades de daño causadas. 
        """ 
        self.surge_mode = self.check_surge_activation()
        
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

    def effectiveness(self, opponent: 'Pokemon') -> int:
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
        """
        Inicializa la subclase GrassPokemon, hereda los atributos de Pokemon y se le asigna un atributo más propio.
        
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
        self.healing = value

    def grass_attack(self, opponent: 'Pokemon') -> int:
        """
        Disminuye la vida del oponente en n unidades de daño.
        
        Parameters:
            opponent (Pokemon): El Pokemon oponente.

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
        Cura al Pokemon con un máximo de n unidades.
        
        Returns:
            int: El número de unidades de puntos de vida efectivas en las que se ha curado el objetivo.
        """
        heal_points = round(self.healing * self.hp)
        healed_hp = heal_points + self.hp
        #not so sure
        if healed_hp > self.total_hp:
            heal_points = self.total_hp - self.hp
            self.hp = self.total_hp
            return heal_points
        elif healed_hp <= self.total_hp:
            self.hp = healed_hp
            return heal_points

    def effectiveness(self, opponent: 'Pokemon') -> int:
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
        Inicializa la subclase FirePokemon, hereda los atributos de Pokemon y se le asigna un atributo más propio.
        
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
        self.temperature = value        

    def fire_attack(self, opponent: 'Pokemon') -> int:
        """
        Disminuye la vida del oponente en n unidades de daño.
        
        Parameters:
            opponent (Pokemon): El Pokemon oponente.

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
        Disminuye la vida del oponente en strength*temperature unidades de daño,.
        
        Parameters:
            opponent (Pokemon): El Pokemon oponente.

        Returns:
            int: El número de unidades de daño causadas. 
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