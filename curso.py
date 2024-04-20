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
            duracion (str): 
            num_alumnos (int):
            nivel (str): ???
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
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._nombre
    
    @property
    def duracion(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._duracion
    
    @property
    def num_alumnos(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._num_alumnos
    
    @property
    def nivel(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._nivel
    @property
    def idioma(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._idioma
    @property
    def precio(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._precio
    