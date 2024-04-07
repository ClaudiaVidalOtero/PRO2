"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es) 
"""
import sys 
from movies import *
from array_ordered_positional_list import ArrayOrderedPositionalList as ArrayOrderedPositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList as LinkedOrderedPositionalList 

class MovieSimulator:
    
    """Una clase que simula la gestión de un catálogo de películas."""
    
    def load_movies_from_file(self, text: str):
        
        """
        Crea las peliculas a partir de un texto dado como entrada y las almacena en una lista posicional ordenada

        Parameters:
            text (str): Texto multilínea que contiene los datos de las peliculas.

        Returns:
            Lista posicional ordenada que contiene las peliculas cargadas desde el archivo.
        """
        movies = LinkedOrderedPositionalList()
        lines = text.split("\n")

        # Iterar sobre cada línea en el texto
        for line in lines:
            # Dividir la línea en sus partes
            parts = line.split('; ')
            # Verificar si la línea tiene la cantidad correcta de elementos
            if len(parts) == 4:
                director = parts[0]
                title = parts[1]
                year = int(parts[2])
                rating = float(parts[3])
                # Crear una instancia de MovieImplementation y agregarla a la lista de películas
                movie = Movie(director, title, year, rating)
                movies.add(movie)
            else:
                print(f"Error: línea mal formateada - {line}")

        return movies
        
    def show_all_movies(self, movies):
        """ Lista todas las películas de la lista posicional ordenada.

        Parameters:
            movies (ArrayOrderedPositionalList): La lista posicional ordenada de películas.
        """
        for movie in movies:
            print(f"{movie.title} ({movie.year}) - Dirigida por: {movie.director} - Rating: {movie.rating}")

           
    def show_movies_by_director(self, movies, director):
        """ Lista las películas de la lista posicional ordenada dirigidas por un director específico.

        Parameters:
            movies (ArrayOrderedPositionalList): La lista posicional ordenada de películas.
            director (str): El nombre del director/a.
        """
        for movie in movies:
            if movie.director == director:
                print(f"{movie.title} ({movie.year}) - Rating: {movie.rating}")

    def show_movies_by_year(self, movies, year):
        """ Lista las películas de la lista posicional ordenada estrenadas en un año específico.

        Parameters:
            movies (ArrayOrderedPositionalList): La lista posicional ordenada de películas.
            year (int): El año de estreno.
        """
        for movie in movies:
            if movie.year == year:
                print(f"{movie.title} - Dirigida por: {movie.director} - Rating: {movie.rating}")

    def show_menu(self):
        """ Muestra el menú de opciones disponibles."""

        print("\n--- Menú ---")
        print("1. Mostrar todas las películas")
        print("2. Buscar películas por director")
        print("3. Buscar películas por año de estreno")
        print("4. Salir")
    
    def execute_menu(self, movies):
        """ Muestra el menú de opciones disponibles y realiza las acciones correspondientes según la opción seleccionada por el usuario.
        
        Parameters:
            movies (ArrayOrderedPositionalList): La lista posicional ordenada de películas.
    """
        while True:
            self.show_menu()
            option = input("Seleccione una opción: ")

            if option == "1":
                print("\n--- Todas las películas ---")
                self.show_all_movies(movies)
            elif option == "2":
                director = input("Introduce el nombre del director/a: ")
                print(f"\n--- Películas dirigidas por {director} ---")
                self.show_movies_by_director(movies, director)
            elif option == "3":
                year = int(input("Introduce el año de estreno: "))
                print(f"\n--- Películas estrenadas en el año {year} ---")
                self.show_movies_by_year(movies, year)
            elif option == "4":
                print("Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """

    with open(sys.argv[1]) as f:
        movies_text = f.read()
        simulator = MovieSimulator()
        movies = simulator.load_movies_from_file(movies_text)
        simulator.execute_menu(movies)

    
if __name__ == '__main__':
    main()