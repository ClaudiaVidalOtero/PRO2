"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import sys
from array_queue import ArrayQueue
from process import Process
from queue_handler import QueueHandler

class QueueSimulator:
    def create_cola_registro(self, text: str):
        cola_registro = ArrayQueue()
        lines = text.split("\t")

        for line in lines:
            parts = line.split()  # Dividir la línea en partes separadas por espacios
            if len(parts) == 5:  # Asegurarse de que haya 5 partes en la línea
                # Extraer los atributos del proceso
                pid = parts[0]
                user_id = parts[1]
                resource_type = parts[2]
                execution_time = parts[3]
                estimated_execution_time = int(parts[4])
                # Crear un proceso y agregarlo a la cola de registro
                proceso = Process(pid, user_id, resource_type, execution_time, estimated_execution_time)
                cola_registro.append(proceso)
        return cola_registro
        


def main():
    
    """
    La función principal que lee desde un archivo y comienza la simulación.
    """

    with open(sys.argv[1]) as f:
        process_text = f.read()
        simulator = QueueSimulator()



if __name__ == "__main__":
    main()
    