"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, name, level, strength, defense, hp, total_hp, agility, pokemon_type):
        """
        Inicializa la clase Pokemon y se le asignan sus atributos.

        Parameters:
            name (str): Nombre del Pokemon.
            level (int): Nivel del Pokemon del 1 hasta al 100.
            strength (int): Fuerza del Pokemon.
            defense (int): Defensa del Pokemon 
            hp (int): Puntos de salud del Pokemon.
            total_hp (int): Puntos de salud total del Pokemon.
            agility (int): Agilidad del Pokemon.
            pokemon_type (str): Tipo de Pokemon.
        """
        self._name = name
        self._level = level
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = pokemon_type


    @property
    def name(self):
        # Property (getter) para name
        return self._name
    
    @property
    def level(self):
        # Property (getter) para level
        return self._level

    @level.setter
    def level(self, value):
        # Setter para level
        self._level = value

    @property
    def strength(self):
        # Property (getter) para strength
        return self._strength

    @strength.setter
    def strength(self, value):
        # Setter para strength
        self._strength = value

    @property
    def defense(self):
        # Property (getter) para defense
        return self._defense   

    @defense.setter
    def defense(self, value):
        # Setter para defense
        self._defense = value

    @property
    def hp(self):
        # Property (getter) para hp
        return self._hp
    
    @hp.setter
    def hp(self, value:int):
        # Setter para hp
        if value >= 0:
            self._hp = value
        else:
            self._hp = 0
    
    @property
    def total_hp(self):
        # Property (getter) para total hp
        return self._total_hp

    @property
    def agility(self):
        # Property (getter) para agility
        return self._agility

    @agility.setter
    def agility(self, value):
        # Setter para agility
        self._agility = value

    @property
    def pokemon_type(self):
        # Property (getter) para pokemon type
        return self._pokemon_type

    @pokemon_type.setter
    def pokemon_type(self, value):
        # Setter para pokemon type
        self._pokemon_type = value
    

    def basic_attack(self, opponent:'Pokemon') -> int:
        """
        Disminuye el valor del atributo hp del oponente ens n unidades de daño.
                
        Parameters:
            opponent (Pokemon): El Pokemon oponente.

        Returns:
            int: El número de unidades de daño que el Pokemon causó a opponent.
        """
        damage = max(1, (self.strength - opponent.defense))
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
    def effectiveness(self, opponent: 'Pokemon') -> int:
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

        info = "{0} ({1}) Stats:".format(self._name, self._pokemon_type)
        info += 'Level: {0}, ATT: {1}, DEF: {2}, AGI: {3}, HP: {4}/{5}.'.format(self._level, self._strength, self._defense, self._agility, self._hp, self._total_hp)
        return info
class WaterPokemon(Pokemon):
    def __init__(self, name, level, strength, defense, hp, total_hp, agility, pokemon_type, surge_mode):
        """
        Inicializa la subclase WaterPokemon, hereda los atributos de Pokemon y se le asigna un atributo más propio.
        
        Parameters:
            surge_mode(bool): Modo oleaje del pokemon sin activar inicialmente.
        """
        self._surge_mode = surge_mode
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type)


    @property
    def surge_mode(self):
        # Property (getter) para surge mode
        return self._surge_mode 
    

    @surge_mode.setter
    def surge_mode(self, value):
        # Setter para surge mode
        self._surge_mode = value


    def check_surge_activation(self) -> bool:
        """
        Verifica si el modo de oleaje debería activarse para un Pokemon si la cantidad de puntos de HP es menor que la mitad de los puntos totales de HP. 
        
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

        damage = max(1, int(factor*self.strength) - opponent.defense)  # En la operación se redondea al número inferior
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
    def __init__(self, name, level, strength, defense, hp, total_hp, agility, pokemon_type, healing):
        """
        Inicializa la subclase GrassPokemon, hereda los atributos de Pokemon y se le asigna un atributo más propio.
        
        Parameters:
            healing (float): La cantidad de curación que posee.
        """
        self._healing = healing
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type)
    

    @property
    def healing(self):
        # Property (getter) para healing
        return self._healing 
    

    @healing.setter
    def healing(self, value: float):
        # Setter para healing
        self._healing = value


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
    
        damage = max(1, int(factor*self.strength) - opponent.defense)  # En la operación se redondea al número inferior 
        opponent.hp -= damage

        return damage
    

    def heal(self) -> int: 
        """
        Cura al Pokemon con un máximo de n unidades.
        
        Returns:
            int: El número de unidades de puntos de vida efectivas en las que se ha curado el objetivo.
        """
        heal_points = int(self.healing * self.hp)
        healed_hp = heal_points + self.hp

        if healed_hp > self.total_hp: # Si el total de HP es menor que el HP curado
            heal_points = self.total_hp - self.hp # Calcula la curación realmente efectiva
            self.hp = self.total_hp # E iguala la vida actual con el total HP ya que no es correcto modificar el total de HP.
            return heal_points 
        else: # Si el total de HP es menor o igual al HP curado 
            self.hp = healed_hp # No hay nada que modificar en el HP curado y se actualiza el HP del Pokemon
            return heal_points # Devuelve los puntos de curación, ya que no se excedió el total de HP y toda la curación fue efectiva.


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
    def __init__(self, name, level, strength, defense, hp, total_hp, agility, pokemon_type, temperature):
        """
        Inicializa la subclase FirePokemon, hereda los atributos de Pokemon y se le asigna un atributo más propio.
        
        Parameters:
            temperature(float): Temperatura del pokemon.
        """
        self._temperature = temperature
        super().__init__(name, level, strength, defense, hp, total_hp, agility, pokemon_type)
    

    @property
    def temperature(self):
        # Property (getter) para temperature
        return self._temperature 
    

    @temperature.setter
    def temperature(self, value):
        # Setter para temperature
        self._temperature = value        


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

        damage = max(1, int(factor*self.strength) - opponent.defense)  # En la operación se redondea al número inferior
        opponent.hp -= damage

        return damage
    

    def embers(self, opponent: 'Pokemon') -> int:
        """
        Disminuye la vida del oponente en strength*temperature unidades de daño.
        
        Parameters:
            opponent (Pokemon): El Pokemon oponente.

        Returns:
            int: El número de unidades de daño causadas. 
        """
        damage = int(self.strength*self.temperature)
        opponent.hp -= damage
        return damage
    
    def effectiveness(self, opponent: 'Pokemon') -> int:
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