"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import sys
import pandas as pd
from curso import Curso
from avl_tree import AVL

class SimuladorAcademias:

    curso_data = []

    def leer_cursos(self, text: str):
        
        """
        Crea los cursos a partir de un texto dado y las almacena en un arbol posicional,
        además, crea una lista para calcular las métricas.

        Parameters:
            text (str): Texto multilínea que contiene los datos de las peliculas.

        Returns:
            Lista posicional ordenada que contiene las peliculas cargadas desde el archivo.
        """
        cursos = AVL()
        lines = text.split("\n")

        # Iterar sobre cada línea en el texto
        for line in lines:
            # Dividir la línea en sus partes
            parts = line.split(',')
            # Verificar si la línea tiene la cantidad correcta de elementos
            if len(parts) == 6:
                nombre = parts[0]
                duracion = int(parts[1])
                num_alumnos = int(parts[2])
                nivel = parts[3]
                idioma = parts[4]
                precio = float(parts[5])
                # Crea una instancia de Curso y la agrega al arbol posicional de cursos
                curso = Curso(nombre, duracion, num_alumnos, nivel, idioma, precio)
                self.insert(cursos, curso)
                # Crea una lista para las métricas
                # self.curso_data.append(Metrics(curso.nombre, curso.duracion, curso.num_alumnos, curso.nivel, curso.idioma, curso.precio)) 
            else:
                print(f"Error: línea mal formateada - {line}")

        return cursos
        
    

    def oferta_agregada(self):
        pass
    def oferta_comun(self):
        pass


class Metrics:
    pass

def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """

    with open(sys.argv[1]) as f:
        cursos_text = f.read()
        simulator = SimuladorAcademias()
        simulator.leer_cursos(cursos_text)
        #simulator.execute_menu(cursos)

    
    print("El archivo no fue encontrado.")
    
if __name__ == '__main__':
    main()