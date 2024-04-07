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
        for line in text:
            # Ayuda no se

        # unique_movies = Movie.delete_duplicates(movies)
        # return unique_movies
            pass 
         
    def list_all_movies(self, movies):
        pass
    def list_movies_by_director(self, movies, director):
        pass
    def list_movies_by_year(self, movies, year):
        pass
    
    def show_menu():
        print("\n--- Menú ---")
        print("1. Mostrar todas las películas")
        print("2. Buscar películas por director")
        print("3. Buscar películas por año de estreno")
        print("4. Salir")
    
    def execute_menu(self, movies):
        while True:
            self.show_menu()
            option = input("Seleccione una opción: ")

            if option == "1":
                print("\n--- Todas las películas ---")
                self.list_all_movies(movies)
            elif option == "2":
                director = input("Introduce el nombre del director/a: ")
                print(f"\n--- Películas dirigidas por {director} ---")
                self.list_movies_by_director(movies, director)
            elif option == "3":
                year = int(input("Introduce el año de estreno: "))
                print(f"\n--- Películas estrenadas en el año {year} ---")
                self.list_movies_by_year(movies, year)
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
        # trainer1, trainer2 = simulator.parse_file()
        # simulator.battle(trainer1, trainer2)
        # estadisticas(simulator)

    
if __name__ == '__main__':
    main()