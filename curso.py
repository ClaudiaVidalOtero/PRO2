"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
from  abc import ABC

class Curso(ABC):
    def __init__(self, nombre: str, duracion: int, num_alumnos: int, nivel: str, idioma: str, precio: int):
        """
        Inicializa la clase Curso y se le asignan sus atributos.
        Parameters:
            nombre (str): 
            duracion (int): 
            num_alumnos (int):
            nivel (str):
            idioma (str)
            precio (int)
        
        """
        self._nombre = nombre
        self._duracion = duracion
        self._num_alumnos = num_alumnos
        self._nivel = nivel
        self._idioma = idioma
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def duracion(self):
        return self._duracion
    
    @property
    def num_alumnos(self):
        return self._num_alumnos
    
    @property
    def nivel(self):
        return self._nivel
    
    @property
    def idioma(self):
        return self._idioma
    @property
    def precio(self):
        return self._precio
    