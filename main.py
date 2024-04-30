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
    """Una clase que simula la gestión de diversos cursos provenientes de dos academias."""
    arbolB_data = []
    arbolA_data = []
    
    def leer_cursos(self, text: str, arbol: str):
        

        """
        Crea los cursos a partir de un texto dado y las almacena en un arbol posicional,
        además, crea una lista para calcular las métricas.

        Parameters:
            text (str): Texto multilínea que contiene los datos de los cursos.
            arbol (str): Nombre del arbol de la academia.

        Returns:
            AVL: un arbol posicional que contiene los cursos.
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
                if arbol == 'arbol_A':
                    self.arbolA_data.append(Metrics(curso.nombre, curso.duracion, curso.num_alumnos, curso.nivel, curso.idioma, curso.precio))
                elif arbol == 'arbol_B':
                    self.arbolB_data.append(Metrics(curso.nombre, curso.duracion, curso.num_alumnos, curso.nivel, curso.idioma, curso.precio))
            else:
                print(f"Error: línea mal formateada - {line}")

        return cursos
    
    def seleccionar_curso_mayor_beneficio(self, curso_A, curso_B):

        """ Selecciona el curso con mayor beneficio entre dos cursos dados (precio por hora y estudiante). 
        El número de estudiantes de los grupos fusionados se sumará.

        Parameters:
            curso_A (Curso): primer curso.
            curso_B (Curso): segundo curso.
        Returns:
            Curso: el curso seleccionado con mayor beneficio entre curso_A y curso_B.
        """

        beneficio_A = curso_A.precio * curso_A.duracion * curso_A.num_alumnos
        beneficio_B = curso_B.precio * curso_B.duracion * curso_B.num_alumnos
        # Seleccionar el curso con mayor beneficio
        if beneficio_A > beneficio_B:
            curso_seleccionado = curso_A
        else:
            curso_seleccionado = curso_B
        # Sumar el número de estudiantes de los grupos fusionados
        num_alumnos_fusionados = curso_A.num_alumnos + curso_B.num_alumnos
        # Actualizar el curso seleccionado con el nuevo número de estudiantes
        curso_seleccionado.num_alumnos = num_alumnos_fusionados

        return curso_seleccionado

    def oferta_agregada(self, arbol_A, arbol_B, nombre_academia_A, nombre_academia_B):
        """
        Combina los cursos de dos árboles de cursos (arbol_A y arbol_B) en un nuevo árbol llamado oferta_agregada.
        Los cursos con claves idénticas se fusionan seleccionando el curso con el mayor beneficio.
        Los cursos con nombres idénticos pero claves diferentes se renombran para indicar la academia de origen.
        
        Parameters:
            arbol_A (AVL): Árbol de cursos de la academia A.
            arbol_B (AVL): Árbol de cursos de la academia B.
            nombre_academia_A (str): Nombre de la academia A.
            nombre_academia_B (str): Nombre de la academia B.
            
        Returns:
            AVL: Un árbol AVL que contiene la oferta agregada de cursos de ambas academias.
        """

        # Crear un nuevo árbol para almacenar la oferta agregada
        oferta_agregada = AVL()

        # Recorrer el árbol de cursos del arbol_A
        for clave_A in arbol_A:
            curso_A = arbol_A.__getitem__(clave_A)
            # Recorrer el árbol de cursos del arbol_B
            for clave_B in arbol_B: 
                curso_B = arbol_B.__getitem__(clave_B)
                if clave_A == clave_B:
                    curso_seleccionado = self.seleccionar_curso_mayor_beneficio(curso_A, curso_B)
                    oferta_agregada[clave_A] = curso_seleccionado

                else:
                    if curso_A.nombre == curso_B.nombre:
                        curso_A.nombre = f"{curso_A.nombre} - {nombre_academia_A}"
                        curso_B.nombre = f"{curso_B.nombre} - {nombre_academia_B}"
                
                oferta_agregada[clave_B] = curso_B

            oferta_agregada[clave_A] = curso_A

        # Imprimir el resultado de la oferta agregada
        for clave in oferta_agregada:
            curso = oferta_agregada.__getitem__(clave)
            print(f"Nombre: {curso.nombre}")
            print(f"Duración: {curso.duracion}")
            print(f"Número de alumnos: {curso.num_alumnos}")
            print(f"Nivel: {curso.nivel}")
            print(f"Idioma: {curso.idioma}")
            print(f"Precio: {curso.precio}")
            print("")
        
        return oferta_agregada
    
    def oferta_comun(self, arbol_A, arbol_B):
        """
        Encuentra y devuelve la oferta común entre dos árboles de cursos (arbol_A y arbol_B).
        La oferta común consiste en cursos que están presentes en ambos árboles, seleccionando el curso
        con el mayor beneficio en caso de existir cursos con claves idénticas.

        Args:
            arbol_A (AVL): Árbol de cursos de la academia A.
            arbol_B (AVL): Árbol de cursos de la academia B.

        Returns:
            AVL: Un árbol AVL que contiene la oferta común de cursos presentes en ambos árboles.
        """

        oferta_comun = AVL()

        for clave_B in arbol_B:
            curso_B = arbol_B.__getitem__(clave_B)
            for clave_A in arbol_A:
                curso_A = arbol_A.__getitem__(clave_A)
                if clave_A == clave_B:
                    curso_seleccionado = self.seleccionar_curso_mayor_beneficio(curso_A, curso_B)
                    oferta_comun[clave_B] = curso_seleccionado

        for clave in oferta_comun:
            curso = oferta_comun.__getitem__(clave)
            print(f"Nombre: {curso.nombre}")
            print(f"Duración: {curso.duracion}")
            print(f"Número de alumnos: {curso.num_alumnos}")
            print(f"Nivel: {curso.nivel}")
            print(f"Idioma: {curso.idioma}")
            print(f"Precio: {curso.precio}")
            print("")

        return oferta_comun
    
    def show_menu(self):
        """ Muestra el menú de opciones disponibles."""
        print("\n--- Menú ---")
        print("1. Leer los ficheros de los cursos e insertarlos en árboles AVL")
        print("2. Operación 'oferta agregada' - cursos realizados por cada academia")
        print("3. Operación 'oferta común' - cursos realizados por ambas academias")
        print("4. Mostrar métricas")
        print("5. Salir")

    def comprobar_cursos_cargados(self):
        """ Comprueba si los cursos de las academias A y B han sido cargados."""
        if not self.arbolA_data or not self.arbolB_data:
            print("Por favor, primero cargue los cursos de las academias A y B (opción 1).")
            return False
        return True

    def execute_menu(self):
        """ 
        Muestra el menú de opciones disponibles y realiza las acciones correspondientes según la opción seleccionada por el usuario.
            
        """
        while True:
            self.show_menu()
            option = input("Seleccione una opción: ")

            if option == "1": # Leer los ficheros de los cursos e insertarlos en árboles AVL
                academia_A = input("Introduce el nombre del archivo txt de la academia A:")
                with open(academia_A) as f:
                    cursosA_text = f.read()
                    cursosA = self.leer_cursos(cursosA_text, 'arbol_A')
                academia_B = input("Introduce el nombre del archivo txt de la academia B:")
                with open(academia_B) as g:
                    cursosB_text = g.read()
                    cursosB = self.leer_cursos(cursosB_text, 'arbol_B')
            elif option == "2": # Operación 'oferta agregada'
                if self.comprobar_cursos_cargados():
                    print("------------ OFERTA AGREGADA ------------")
                    self.oferta_agregada(cursosA, cursosB, "Academia A", "Academia B")
            elif option == "3": # Operación 'oferta común'
                if self.comprobar_cursos_cargados():
                    print("------------ OFERTA COMÚN ------------")
                    self.oferta_comun(cursosA, cursosB)
            elif option == "4": # Mostrar métricas
                if self.comprobar_cursos_cargados():
                    metrics(self)
            elif option == "5": # Salir
                print("Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

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
    
    @property
    def curso_ingresos(self):
        return self._curso_ingresos

def metrics(self):
        """Crea las estadísticas pedidas por el enunciado."""

        #CREAMOS UN DATAFRAME CON LOS DATOS DE CADA CURSO POR CADA ARBOL.
        print("DATAFRAME DEL ARBOL A:")
        data_A = pd.DataFrame([
            {"nombre": metrics._nombre, "duracion": metrics._duracion, "num_alumnos": metrics._num_alumnos, 
            "nivel": metrics._nivel, "idioma": metrics._idioma, "precio": metrics._precio}
        for metrics in self.arbolA_data])
        print(data_A)

        print("DATAFRAME DEL ARBOL B:")
        data_B = pd.DataFrame([
            {"nombre": metrics._nombre, "duracion": metrics._duracion, "num_alumnos": metrics._num_alumnos, 
            "nivel": metrics._nivel, "idioma": metrics._idioma, "precio": metrics._precio}
        for metrics in self.arbolB_data])
        print(data_B)

        #ESTADÍSTICAS DE LA SIMULACIÓN USANDO PANDAS. 

        #(1) Número medio de alumnos por idioma.
        group_col = "idioma"
        target_col = "num_alumnos"
        data_cursoA = data_A.groupby(group_col).agg({target_col :["mean"]})

        print("\n")
        print ("ALUMNOS GROUP BY IDIOMA ARBOL A")
        print (data_cursoA)

        data_cursoB = data_B.groupby(group_col).agg({target_col :["mean"]})
        print("\n")
        print ("ALUMNOS GROUP BY IDIOMA ARBOL B")
        print (data_cursoB)

        #2) Número medio de alumnos por nivel. 
        group_col = "nivel"
        target_col = "num_alumnos"

        data_cursoA = data_A.groupby(group_col).agg({target_col :["mean"]})

        print("\n")
        print ("ALUMNOS GROUP BY NIVEL ARBOL A")
        print (data_cursoA)
        
        data_cursoB = data_B.groupby(group_col).agg({target_col :["mean"]})

        print("\n")
        print ("ALUMNOS GROUP BY NIVEL ARBOL B")
        print (data_cursoB)

        #3) Ingresos totales posibles.
        total_income_A = (data_A['precio'] * data_A['duracion'] * data_A['num_alumnos']).sum()
        total_income_B = (data_B['precio'] * data_B['duracion'] * data_B['num_alumnos']).sum()

        print("\n")
        print("TOTAL POSSIBLE INCOME FOR CURSOS A")
        print(total_income_A)

        print("\n")
        print("TOTAL POSSIBLE INCOME FOR CURSOS B")
        print(total_income_B)

def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """
    simulator = SimuladorAcademias()
    simulator.execute_menu()
    
if __name__ == '__main__':
    main()