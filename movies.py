"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es) 
"""
from abc import ABC

class Movie(ABC):
    def __init__(self, director: str, title: str, year: int, rating: int):
        """
        Inicializa la clase Movie y se le asignan sus atributos.
        Parameters:
            director (str): Director de la película.
            title (str): Título de la película.
            year (int): Año de estreno.
            rating (int): Puntuación de la película por el público.
        """
        self._director = director
        self._title = title
        self._year = year
        self._rating = rating

    @property
    def director(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._director
    
    @property
    def title(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._title
    
    @property
    def year(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._year
    
    @property
    def rating(self):
        """Ejemplo de uso propiedades (en vez de getter)"""
        return self._rating
    @rating.setter
    def rating(self, rating: int):
        """Ejemplo de uso propiedades (en vez de setter)"""
        if rating > 0 and rating <= 10:
            self._rating = rating
        else:
            raise ValueError("Rating must be between 1 and 10.")


    def __str__(self):
        return f"{self.director} ({self.year}) {self.title} - Rating: {self.rating}"

    def __lt__(self, other):
        """ 
        Comprueba si el objeto actual es menor que otro objeto.

        Parameters:
            other: Otro objeto con el que se va a comparar.
        Returns:
            bool: True si el objeto actual es menor que el otro objeto, False de lo contrario.
        """
        if self.director != other.director:
            return self.director < other.director
        elif self.year != other.year:
            return self.year < other.year
        elif self.title != other.title:
            return self.title < other.title

    def __le__(self, other):
        """ Comprueba si el objeto actual es menor o igual que otro objeto."""
        return self == other or self < other