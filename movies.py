"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es) 
"""
from abc import ABC, abstractmethod
from array_ordered_positional_list import ArrayOrderedPositionalList as ArrayOrderedPositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList as LinkedOrderedPositionalList 

class Movie(ABC):
    def __init__(self, director, title, year, rating):
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

    
    def delete_duplicates(self, movies):
        unique_movies = LinkedOrderedPositionalList() 
        unique_titles = {} # Creamos un diccionario para almacenar las películas únicas basadas en el título y el director.

        for movie in movies:
            # Verificamos si el título y director de la película actual ya están en el diccionario de películas únicas.
            if (movie.title, movie.director) in unique_titles:
                # Si ya hay una película con el mismo título y director, comparamos los años de estreno.
                existing_movie = unique_titles[(movie.title, movie.director)]
                if movie.year > existing_movie.year:
                    unique_titles[(movie.title, movie.director)] = movie
            else:
                unique_titles[(movie.title, movie.director)] = movie
        
        # Agregamos las películas únicas del diccionario a la lista de películas únicas.
        for movie in unique_titles.values():
            unique_movies._add_last(movie)

        return unique_movies