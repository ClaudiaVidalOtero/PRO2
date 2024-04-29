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
                cursos[clave] = curso
                # Crea una lista para las métricas
                # self.curso_data.append(Metrics(curso.nombre, curso.duracion, curso.num_alumnos, curso.nivel, curso.idioma, curso.precio)) 
            else:
                print(f"Error: línea mal formateada - {line}")

        return cursos
    
    
    def oferta_agregada(self, arbol_origen, arbol_destino, nombre_academia_origen, nombre_academia_destino):

        # Crear un nuevo árbol para almacenar la oferta agregada
        oferta_agregada = AVL()

        # Recorrer el árbol de cursos del arbol_origen
        for clave in arbol_origen:

            curso_origen = arbol_origen[clave]
            # Verificar si el curso existe en el arbol_destino
            if clave in arbol_destino:
                curso_destino = arbol_destino[clave]
                # Verificar si los cursos tienen el mismo nombre
                if curso_origen.nombre == curso_destino.nombre:
                    # Calcular el beneficio por hora y estudiante de cada curso
                    beneficio_origen = curso_origen.precio / (curso_origen.duracion * curso_origen.num_alumnos)
                    beneficio_destino = curso_destino.precio / (curso_destino.duracion * curso_destino.num_alumnos)
                    # Seleccionar el curso con mayor beneficio
                    if beneficio_origen > beneficio_destino:
                        curso_seleccionado = curso_origen
                    else:
                        curso_seleccionado = curso_destino
                    curso_seleccionado.nombre = f"{curso_seleccionado.nombre} - {nombre_academia_origen} - {nombre_academia_destino}"
                    # Sumar el número de estudiantes de los grupos fusionados
                    num_alumnos_fusionados = curso_origen.num_alumnos + curso_destino.num_alumnos
                    # Actualizar el curso seleccionado con el nuevo número de estudiantes
                    curso_seleccionado.num_alumnos = num_alumnos_fusionados
                    # Agregar el curso seleccionado al árbol de oferta agregada
                    oferta_agregada[clave] = curso_seleccionado
                else:
                    # Añadir el nombre de la compañía al curso del arbol_destino
                    curso_destino.nombre = f"{curso_destino.nombre} - {nombre_academia}"
                    # Agregar el curso del arbol_destino al árbol de oferta agregada
                    oferta_agregada[clave] = curso_destino
            else:
                # Agregar el curso del arbol_origen al árbol de oferta agregada
                oferta_agregada[clave] = curso_origen

        # Recorrer el árbol de cursos del arbol_destino
        for clave, curso_destino in arbol_destino.items():
            # Verificar si el curso no existe en el árbol de oferta agregada
            if clave not in oferta_agregada:
                # Añadir el nombre de la compañía al curso del arbol_destino
                curso_destino.nombre = f"{curso_destino.nombre} - {nombre_academia}"
                # Agregar el curso del arbol_destino al árbol de oferta agregada
                oferta_agregada[clave] = curso_destino

            # Imprimir el resultado de la oferta agregada
        for clave, curso in oferta_agregada.items():
            print(f"Curso: {curso.nombre}")
            print(f"Duración: {curso.duracion}")
            print(f"Número de alumnos: {curso.num_alumnos}")
            print(f"Nivel: {curso.nivel}")
            print(f"Idioma: {curso.idio
                             ma}")
            print(f"Precio: {curso.precio}")
            print("")

        return oferta_agregada
    
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