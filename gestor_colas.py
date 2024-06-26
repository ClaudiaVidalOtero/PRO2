"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es) 
"""

from array_queue import ArrayQueue
import pandas as pd
from collections import defaultdict

class GestorColas:
    """
    Inicializa la clase GestorColas y se le asignan sus atributos.

    Parameters:
        cpu_short_queue (ArrayQueue): Cola para procesos cortos de CPU.
        cpu_long_queue (ArrayQueue): Cola para procesos largos de CPU.
        gpu_short_queue (ArrayQueue): Cola para procesos cortos de GPU.
        gpu_long_queue (ArrayQueue): Cola para procesos largos de GPU.
        running_processes (dict): Diccionario con los procesos actualmente en ejecución, clasificados por tipo de cola.
        penalizaciones (dict): Diccionario de penalizaciones activas por usuario.
        penalizaciones_activas (defaultdict): Diccionario que cuenta el número de penalizaciones aplicadas por usuario.
        lista_datos_procesos (list): Lista de datos de procesos usados para análisis y estadísticas.
    """
    def __init__(self):
        self.cpu_short_queue = ArrayQueue()
        self.cpu_long_queue = ArrayQueue()
        self.gpu_short_queue = ArrayQueue()
        self.gpu_long_queue = ArrayQueue()
        self.running_processes = {
            'cpu_short': None,
            'cpu_long': None,
            'gpu_short': None,
            'gpu_long': None
        }
        self.penalizaciones = {}
        self.penalizaciones_activas = defaultdict(int)
        self.lista_datos_procesos = []

    def agregar_proceso(self, proceso, tiempo_actual):
        """
        Agrega un proceso a la cola de ejecución correspondiente según su tipo de recurso y tiempo estimado.
        Parameters:
            proceso (Proceso): El proceso a agregar a la cola de ejecución.
            tiempo_actual (int): El tiempo actual de la simulación en unidades de tiempo.
        """
        proceso.tiempo_entrada = tiempo_actual
        if proceso.tipo_recurso == 'cpu' and proceso.tiempo_estimado == 'short':
            self.cpu_short_queue.enqueue(proceso)
        elif proceso.tipo_recurso == 'cpu' and proceso.tiempo_estimado == 'long':
            self.cpu_long_queue.enqueue(proceso)
        elif proceso.tipo_recurso == 'gpu' and proceso.tiempo_estimado == 'short':
            self.gpu_short_queue.enqueue(proceso)
        elif proceso.tipo_recurso == 'gpu' and proceso.tiempo_estimado == 'long':
            self.gpu_long_queue.enqueue(proceso)

    def iniciar_proceso(self, tipo_cola, tiempo_actual):
        """
        Inicia un proceso en la cola de ejecución si no hay procesos actualmente en ejecución en la cola especificada.
        Parameters:
            tipo_cola (str): El tipo de cola de ejecución del proceso.
            tiempo_actual (int): El tiempo actual de la simulación en unidades de tiempo.
        """
        queue_map = {
            'cpu_short': self.cpu_short_queue,
            'cpu_long': self.cpu_long_queue,
            'gpu_short': self.gpu_short_queue,
            'gpu_long': self.gpu_long_queue
        }
        if self.running_processes[tipo_cola] is None:
            queue = queue_map[tipo_cola]
            if not queue.is_empty():
                proceso = queue.first()
                if proceso.tiempo_estimado == 'short' and self.penalizaciones.get(proceso.id_usuario, False):
                    queue.dequeue()
                    long_queue = queue_map[tipo_cola.replace('short', 'long')]
                    long_queue.enqueue(proceso)
                    self.penalizaciones[proceso.id_usuario] = False
                    self.penalizaciones_activas[proceso.id_usuario] += 1
                    print(f"Penalización aplicada: {tiempo_actual} {proceso.pid} {proceso.id_usuario}")
                else:
                    queue.dequeue()
                    proceso.tiempo_inicio = tiempo_actual
                    self.running_processes[tipo_cola] = proceso
                    self.lista_datos_procesos.append({
                        'pid': proceso.pid,
                        'id_usuario': proceso.id_usuario,
                        'tipo_cola': tipo_cola,
                        'tiempo_entrada': proceso.tiempo_entrada,
                        'tiempo_inicio': proceso.tiempo_inicio,
                        'tiempo_estimado': proceso.tiempo_estimado,
                        'tiempo_ejecucion': proceso.tiempo_ejecucion
                    })
                    print(f"Proceso añadido a cola de ejecución: {tiempo_actual} {proceso.pid} {proceso.id_usuario} {proceso.tipo_recurso} {proceso.tiempo_estimado}")

    def terminar_proceso(self, tipo_cola, tiempo_actual):
        """
        Termina un proceso en ejecución si ha alcanzado su tiempo de finalización y aplica penalizaciones si es necesario.
        Parameters:
            tipo_cola (str): El tipo de cola de ejecución del proceso.
            tiempo_actual (int): El tiempo actual de la simulación en unidades de tiempo.
        """
        proceso = self.running_processes[tipo_cola]
        if proceso and tiempo_actual >= proceso.tiempo_inicio + proceso.tiempo_ejecucion:
            print(f"Proceso terminado: {tiempo_actual} {proceso.pid} {proceso.id_usuario} {proceso.tipo_recurso} {proceso.tiempo_estimado} {proceso.tiempo_entrada} {proceso.tiempo_inicio} {proceso.tiempo_ejecucion}")
            self.running_processes[tipo_cola] = None
            if proceso.tiempo_estimado == 'short' and proceso.tiempo_ejecucion > 5:
                self.penalizaciones[proceso.id_usuario] = True
                print(f"Penalización activa: {tiempo_actual} {proceso.id_usuario}")

    def estadisticas(self):
        """
        Crea un DataFrame con los datos de cada proceso almacenados en `self.lista_datos_procesos`
        y calcula diversas estadísticas usando pandas.
        """
        # Creamos un DataFrame con los datos de cada proceso
        data = pd.DataFrame(self.lista_datos_procesos)
        print(data)

        # Estadísticas de la simulación usando pandas
        
        # (1) Número medio de procesos a los que se ha aplicado una penalización, agrupado por usuario
        penalizaciones_data = [{'id_usuario': user, 'penalizaciones': count} for user, count in self.penalizaciones_activas.items()]
        penalizaciones_df = pd.DataFrame(penalizaciones_data)
        penalizaciones_df = penalizaciones_df.groupby('id_usuario').agg({'penalizaciones': 'mean'})
        print("\nPenalizaciones promedio por usuario:")
        print(penalizaciones_df)

        # (2) Tiempo medio de permanencia de los procesos en el gestor de colas, agrupado por cola de ejecución
        data['tiempo_permanencia'] = data['tiempo_inicio'] - data['tiempo_entrada']
        tiempos_df = data.groupby('tipo_cola').agg({'tiempo_permanencia': 'mean'}).reset_index()
        print("\nTiempo promedio de permanencia por cola de ejecución:")
        print(tiempos_df)

