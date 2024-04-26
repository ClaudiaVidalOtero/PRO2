"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import sys
import pandas as pd
from curso import Curso
from avl_tree import AVL
from binary_search_tree import *
class SimuladorAcademias:

    curso_data = []

    def leer_cursos(self, text: str):
        
        """
        Crea los cursos a partir de un texto dado y las almacena en un arbol posicional,
        además, crea una lista para calcular las métricas.

        Parameters:
            text (str): Texto multilínea que contiene los datos de los cursos.

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
                clave = (curso.nombre, curso.nivel, curso.idioma)
                cursos.__setitem__(clave, curso)
                # cursos[clave] = curso
                # cursos.__getitem__(clave)
                print(clave)
                # Crea una lista para las métricas
                # self.curso_data.append(Metrics(curso.nombre, curso.duracion, curso.num_alumnos, curso.nivel, curso.idioma, curso.precio)) 
            else:
                print(f"Error: línea mal formateada - {line}")

        return cursos
    
    def oferta_agregada(arbol_origen, arbol_destino, nombre_academia):

        for _, curso in arbol_origen.algo: #(algo q devuelva los valores de cada nodo):
            nombre_curso = curso.nombre
            nivel_curso = curso.nivel
            idioma_curso = curso.idioma
            
            # Buscar el curso en el árbol destino
            nodo = arbol_destino._subtree_search(arbol_destino.root(), (nombre_curso, nivel_curso, idioma_curso))
            
            # Si el curso ya está en el árbol destino, actualizar o fusionar
            if nodo is not None and nodo.key() == (nombre_curso, nivel_curso, idioma_curso):
                curso_destino = nodo.value()
                # Comparar los cursos y seleccionar el de mayor beneficio
                if curso.beneficio() > curso_destino.beneficio():
                    # Reemplazar el curso en el árbol destino con el de mayor beneficio
                    arbol_destino._replace(nodo, ((nombre_curso, nivel_curso, idioma_curso), curso))
                # Sumar el número de estudiantes
                curso_destino.num_alumnos += curso.num_alumnos
            else:
                # Agregar el curso al árbol destino
                # Si el nombre del curso ya existe en el árbol destino, añadir el nombre de la compañía
                if nodo is not None and nodo.key()[0] == nombre_curso:
                    nombre_curso += f' ({nombre_academia})'
                # Agregar el curso al árbol destino
                arbol_destino.__setitem__(nombre_curso, (nombre_curso, nivel_curso, idioma_curso))

        print(arbol_destino)

    def oferta_comun(self):
        pass
    

class Metrics:
    """
    Clase para representar estadísticas de los cursos.

    Parameters:
        nombre (str): nombre del curso.
        duracion (int): duración del curso en minutos.
        num_alumnos (int): número de participantes del curso.
        nivel (str): nivel de difcultad del curso.
        idioma (str): idioma en el que se imparte el curso.
        precio (int): precio por persona del curso.
        
    """
    def __init__(self, nombre: str, duracion: int, num_alumnos: int, nivel: str, idioma: str, precio: int):

    
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
    

def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """
    simulator = SimuladorAcademias()
    with open(sys.argv[1]) as f:
        cursosA_text = f.read()
        simulator.leer_cursos(cursosA_text)
    with open(sys.argv[2]) as g:
        cursosB_text = g.read()
        simulator.leer_cursos(cursosB_text)
        # simulator.oferta_agregada(cursosA, cursosB)

        #simulator.execute_menu(cursos)

    
if __name__ == '__main__':
    main()