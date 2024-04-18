"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es) 
"""
import sys 
import pandas
from movies import *
from array_ordered_positional_list import ArrayOrderedPositionalList as PositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList as PositionalList 

class MovieSimulator:
    
    """Una clase que simula la gestión de un catálogo de películas de una plataforma de streaming."""
    movie_data = []

    def load_movies_from_file(self, text: str):
        
        """
        Crea las peliculas a partir de un texto dado como entrada y las almacena en una lista posicional ordenada

        Parameters:
            text (str): Texto multilínea que contiene los datos de las peliculas.

        Returns:
            Lista posicional ordenada que contiene las peliculas cargadas desde el archivo.
        """
        movies = PositionalList()
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
                self.movie_data.append(Estadistica(movie.director, movie.title, movie.year, movie.rating))
                movies.add(movie)
            else:
                print(f"Error: línea mal formateada - {line}")

        return movies
    
    def delete_duplicates(self, movies):
        """ 
        Elimina las películas duplicadas de la lista de películas dada, manteniendo solo la versión más reciente de cada película.

        Parameters:
            movies (PositionalList): Una lista de películas.
        Returns:
            PositionalList: Una lista de películas sin duplicados, ordenada por autor, año de estreno y título.
        """
        unique_movies = PositionalList() 
        unique_titles = PositionalList() # Creamos una lista ordenada para almacenar las películas únicas basadas en el título y el director.
        terminado = False
        
        p1 = movies.first()
        while not terminado: 
            if p1 is None:
                terminado = True

            else:
                p2 = movies.after(p1)
                movie1 = movies.get_element(p1)
                if p2 is None:
                    unique_titles.add(movie1)
                    terminado = True 
                else:
                    movie2 = movies.get_element(p2)
                    
                if movie1.title != movie2.title or movie2 is None:
                
                    unique_titles.add(movie1)
                    if movie2 is None:
                        terminado = True
                        

                p1 = p2

        # Agregar las películas únicas de la lista de títulos únicos a la lista de películas únicas.
        for movie in unique_titles:
            unique_movies._add_last(movie)

        return unique_movies
        
    def show_all_movies(self, movies):
        """ 
        Imprime todas las películas de la lista posicional ordenada.

        Parameters:
            movies (PositionalList): La lista posicional ordenada de películas.
        """
        for movie in movies:
            print(f"{movie.director} ({movie.year}) {movie.title} - Rating: {movie.rating}")

    def show_movies_by_director(self, movies, director):
        """ 
        Imprime las películas de la lista posicional ordenada dirigidas por un director específico.

        Parameters:
            movies (PositionalList): La lista posicional ordenada de películas.
            director (str): El nombre del director/a.
        """
        for movie in movies:
            if movie.director == director:
                print(f"{movie.title} ({movie.year}) - Rating: {movie.rating}")

    def show_movies_by_year(self, movies, year):
        """ 
        Imprime las películas de la lista posicional ordenada estrenadas en un año específico.

        Parameters:
            movies (PositionalList): La lista posicional ordenada de películas.
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
        print("4. Generar nuevo archivo con las películas ordenadas y sin duplicados")
        print("5. Mostrar métricas")
        print("6. Salir")
    
    def execute_menu(self, movies):
        """ 
        Muestra el menú de opciones disponibles y realiza las acciones correspondientes según la opción seleccionada por el usuario.
        
        Parameters:
            movies (PositionalList): La lista posicional ordenada de películas.
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
            elif option == "4": # Genera nuevo archivo con las películas ordenadas y sin duplicados
                unique_movies = self.delete_duplicates(movies) 
                self.save_movies_to_file(unique_movies, "peliculas_ordenadas")
            elif option == "5": # Mostrar métricas
                estadisticas(self)
            elif option == "6":
                print("Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def save_movies_to_file(self, movies, filename):
        """ Guarda las películas en un archivo.

        Parameters:
            movies (PositionalList): La lista de películas.
            filename (str): El nombre del archivo de salida.
        """
        with open(filename, 'w') as f:
            for movie in movies:
                f.write(f"{movie.director}; {movie.title}; {movie.year}; {movie.rating}\n")
    
class Estadistica:
    """
    Clase para representar estadísticas de una película.
    Parameters:
            director (str): Director de la película.
            title (str): Título de la película.
            year (int): Año de estreno.
            rating (float): Puntuación de la película por el público.
    """
    def __init__(self, director: str, title: str, year: int, rating: int):

        self._director = director
        self._title = title
        self._year = year
        self._rating = rating

    @property
    def director(self):
        # Property (getter) para director
        return self._director

    @property
    def p_type(self):
        # Property (getter) para title
        return self._title  
    
    @property
    def year(self):
        # Property (getter) para year
        return self._year

    @property
    def opponent_type(self):
        # Property (getter) para rating
        return self._rating
    

def estadisticas(self):
        """Crea las estadísticas pedidas por el enunciado."""
        #CREAMOS UN DATAFRAME CON LOS DATOS DE CADA PELÍCULA.
        print("DATAFRAME:")
        data = pandas.DataFrame([
            {"director": estadistica._director, "title": estadistica._title, "year": estadistica._year, 
            "rating": estadistica._rating}
        for estadistica in self.movie_data ])
        print(data)

        #ESTADÍSTICAS DE LA SIMULACIÓN USANDO PANDAS.
        
        #(1) Número de películas por director/a.
        group_col = "director"
        target_col = "title"
        data_movie = data.groupby(group_col).agg({target_col :["nunique"]})

        print("\n")
        print ("MOVIES GROUPED BY DIRECTOR")
        print (data_movie)


        #2) Puntuación media por director/a.
        group_col = "director"
        target_col = "rating"
        data_movie = data.groupby(group_col).agg({target_col :["mean"]})
        
        print("\n")
        print ("RATINGS GROUP BY DIRECTOR")
        print (data_movie)


        #(3) Puntuación media por año de estreno.
        group_col = "year"
        target_col = "rating"
        data_movie = data.groupby(group_col).agg({target_col :["mean"]})

        print("\n")
        print ("RATINGS GROUP BY YEAR")
        print (data_movie)

def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """
    try:
        namefile = input("Ingrese el nombre del archivo de películas: ")
        with open(namefile) as f:
            movies_text = f.read()
            simulator = MovieSimulator()
            movies = simulator.load_movies_from_file(movies_text)
            simulator.execute_menu(movies)

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    
if __name__ == '__main__':
    main()