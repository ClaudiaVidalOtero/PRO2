"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import sys
from array_queue import ArrayQueue
from process import Proceso
from gestor_colas import GestorColas

class QueueSimulator:
    def __init__(self):
        self.processes = ArrayQueue()
        self.gestor = GestorColas()
        self.tiempo_actual = 0

    def leer_procesos(self, text: str):
        """
        Crea los procesos a partir de un texto dado y las almacena en una cola de registro de procesos.

        Parameters:
            text (str): Texto multilínea que contiene los datos de los procesos.
        """
        lines = text.strip().split("\n")

        # Iterar sobre cada línea en el texto
        for line in lines:
            # Dividir la línea en sus partes
            parts = line.split()
            # Verificar si la línea tiene la cantidad correcta de elementos
            if len(parts) == 5:
                pid = parts[0]
                id_usuario = parts[1]
                tipo_recurso = parts[2]
                tiempo_estimado = parts[3]
                tiempo_ejecucion = int(parts[4])
                proceso = Proceso(pid, id_usuario, tipo_recurso, tiempo_estimado, tiempo_ejecucion)
                self.processes.enqueue(proceso)
            else:
                print(f"Error: línea mal formateada - {line}")

        return self.processes


    def simular(self):
        while not self.processes.is_empty() or any([
            not self.gestor.cpu_short_queue.is_empty(),
            not self.gestor.cpu_long_queue.is_empty(),
            not self.gestor.gpu_short_queue.is_empty(),
            not self.gestor.gpu_long_queue.is_empty(),
            self.gestor.running_processes['cpu_short'] is not None,
            self.gestor.running_processes['cpu_long'] is not None,
            self.gestor.running_processes['gpu_short'] is not None,
            self.gestor.running_processes['gpu_long'] is not None
        ]):
            self.tiempo_actual += 1

            if not self.processes.is_empty():
                proceso = self.processes.dequeue()
                self.gestor.agregar_proceso(proceso, self.tiempo_actual)

            for tipo_cola in ['cpu_short', 'cpu_long', 'gpu_short', 'gpu_long']:
                self.gestor.terminar_proceso(tipo_cola, self.tiempo_actual)
                self.gestor.iniciar_proceso(tipo_cola, self.tiempo_actual)
    
        self.gestor.estadisticas()


def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """
    with open(sys.argv[1], 'r') as f:
        text = f.read()      
        simulator = QueueSimulator()
        simulator.leer_procesos(text)
        simulator.simular()
        
if __name__ == '__main__':
    main()