"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import pandas
from curso import Curso

class SimuladorAcademias:
    pass



def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """
    try:
        namefile = input("Ingrese el nombre del archivo de las academias: ")
        with open(namefile) as f:
            cursos_text = f.read()
            simulator = SimuladorAcademias()
            cursos = simulator.load_movies_from_file(cursos_text)
            simulator.execute_menu(cursos)

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    
if __name__ == '__main__':
    main()