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
    
    """Una clase que simula la gestión de un catálogo de películas de una plataforma de streaming.."""
    
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
                movies.add(movie)
            else:
                print(f"Error: línea mal formateada - {line}")

        return movies
    
    def delete_duplicates(self, movies):
        """ Elimina las películas duplicadas de la lista de películas dada, manteniendo solo la versión más reciente de cada película.

        Parameters:
            movies (PositionalList): Una lista de películas.
        Returns:
            PositionalList: Una lista de películas sin duplicados, ordenada por autor, año de estreno y título.
    """
        unique_movies = PositionalList() 
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
            unique_movies.add(movie)

        return unique_movies
    
    def show_all_movies(self, movies):
        """ Imprime todas las películas de la lista posicional ordenada.

        Parameters:
            movies (PositionalList): La lista posicional ordenada de películas.
        """
        for movie in movies:
            print(f"{movie.director} ({movie.year}) {movie.title} - Rating: {movie.rating}")

    def show_movies_by_director(self, movies, director):
        """ Imprime las películas de la lista posicional ordenada dirigidas por un director específico.

        Parameters:
            movies (PositionalList): La lista posicional ordenada de películas.
            director (str): El nombre del director/a.
        """
        for movie in movies:
            if movie.director == director:
                print(f"{movie.title} ({movie.year}) - Rating: {movie.rating}")

    def show_movies_by_year(self, movies, year):
        """ Imprime las películas de la lista posicional ordenada estrenadas en un año específico.

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
        print("4. Salir")
    
    def execute_menu(self, movies):
        """ Muestra el menú de opciones disponibles y realiza las acciones correspondientes según la opción seleccionada por el usuario.
        
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
            elif option == "4":
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
class Metricas:
    """
    Clase para generar métricas relacionadas con las películas.
    """

    def generate_metrics_per_director(self, movies):
        """ Genera métricas por director.

        Parameters:
            movies (list): Lista de películas.

        Yields:
            Tuple: Una tupla con el nombre del director, el número de películas dirigidas por el director y la puntuación media de las películas dirigidas por el director.
        """
        # Dictionary to store the number of movies and the sum of ratings per director
        metrics_per_director = {}

        for movie in movies:
            if movie.director in metrics_per_director:
                num_movies, total_ratings = metrics_per_director[movie.director]
                metrics_per_director[movie.director] = (num_movies + 1, total_ratings + movie.rating)
            else:
                metrics_per_director[movie.director] = (1, movie.rating)

        for director, (num_movies, total_ratings) in metrics_per_director.items():
            yield director, num_movies, total_ratings / num_movies

    def generate_metrics_per_year(self, movies):
        """ Genera métricas por año de estreno.

        Parameters:
            movies (list): Lista de películas.

        Yields:
            Tuple: Una tupla con el año de estreno, el número de películas estrenadas ese año y la puntuación media de las películas estrenadas ese año.
        """
        # Dictionary to store the number of movies and the sum of ratings per release year
    
class Estadistica:
    """
    Clase para representar estadísticas de un pokémon en combate.

    Parameters:
        p_type (str): Tipo del personaje.
        name (str): Nombre del personaje.
        damage (int): Daño que el personaje infringió en su ronda.
        opponent_type (str): Tipo de oponente contra el que el pokemon se enfrenta.
        gained_healing (int): Cantidad de curación que el personaje realiza en su ronda.
    """
    def __init__(self, p_type:str, name:str, damage:int, opponent_type:str, gained_healing:int):
        self._p_type = p_type
        self._name = name
        self._damage = damage
        self._opponent_type = opponent_type
        self._gained_healing = gained_healing 
    @property
    def name(self):
        # Property (getter) para name
        return self._name

    @property
    def p_type(self):
        # Property (getter) para tipo pokemon
        return self._p_type    
    @p_type.setter
    def p_type(self, value):
        # Setter para level
        self._p_type = value

    @property
    def damage(self):
        # Property (getter) para strength
        return self._damage
    @damage.setter
    def damage(self, value):
        # Setter para strength
        self._damage = value

    @property
    def opponent_type(self):
        # Property (getter) para strength
        return self._opponent_type
    @opponent_type.setter
    def strength(self, value):
        # Setter para strength
        self._opponent_type = value
    
    @property
    def gained_healing(self):
        # Property (getter) para strength
        return self._gained_healing
    @gained_healing.setter
    def gained_healing(self, value):
        # Setter para strength
        self._gained_healing = value

    def estadisticas(self):
    #CREAMOS UN DATAFRAME CON LOS DATOS DE CADA RONDA.
        data = pandas.DataFrame([
            {"name": estadistica._name, "type": estadistica._p_type, "damage": estadistica._damage, 
            "opponent_type": estadistica._opponent_type, "healing": estadistica._gained_healing}
        for estadistica in self.lista_datos_pokemon ])
        print(data)


    #ESTADÍSTICAS DE LA SIMULACIÓN USANDO PANDAS
    
    #(1) El daño promedio causado por cada Pokémon individualmente.
    group_col = "name"
    target_col = "damage"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})

    print("\n")
    print ("DAMAGE GROUPED BY NAME")
    print (data_pokemon)


    #2) El daño promedio causado por los Pokémon de cada tipo (agua, fuego, planta)
    group_col = "type"
    target_col = "damage"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})
    
    print("\n")
    print ("DAMAGE GROUPED BY TYPE")
    print (data_pokemon)


    #(3) El daño promedio que cada tipo de Pokémon inflige a cada uno de los otros tipos.
    group_col = ["type","opponent_type"]
    target_col = "damage"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})

    print("\n")
    print ("DAMAGE GROUPED BY (TYPE, OPPONENT_TYPE) ")
    print (data_pokemon)


    #(4) La curación promedia realizada por cada Pokémon.
    group_col = "name"
    target_col = "healing"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})

    print("\n")
    print ("HEALING GROUPED BY NAME")
    print (data_pokemon)

    #(5) La curación promedia realizada por los Pokémon de cada tipo.
    group_col = "type"
    target_col = "healing"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})

    print("\n")
    print ("HEALING GROUPED BY TYPE")
    print (data_pokemon)
    print("\n")

    def mostrar_metricas(self, movies):
        """ Muestra las métricas generadas.

        Parameters:
            movies (list): Lista de películas.
        """

        print("NUMERO DE PELICULAS POR DIRECTOR:")
        for director, num_peliculas, _ in self.generate_metrics_per_director(movies):
            print(f"{director}: {num_peliculas}")

        print("\nPUNTUACION MEDIA POR DIRECTOR:")
        for director, _, puntuacion_media in self.generate_metrics_per_director(movies):
            print(f"{director}: {puntuacion_media:.2f}")

        print("\nPUNTUACION MEDIA POR AÑO DE ESTRENO:")
        for year, _, puntuacion_media in self.generate_metrics_per_year(movies):
            print(f"Año {year}: {puntuacion_media:.2f}")

def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """

    with open(sys.argv[1]) as f:
        movies_text = f.read()
        simulator = MovieSimulator()
        metricas = Metricas()
        movies = simulator.load_movies_from_file(movies_text)
        unique_movies = simulator.delete_duplicates(movies) # Guardar películas ordenadas en un nuevo archivo
        simulator.save_movies_to_file(unique_movies, "peliculas_ordenadas.txt")
        simulator.execute_menu(movies)
        metricas.mostrar_metricas(unique_movies)
    
if __name__ == '__main__':
    main()