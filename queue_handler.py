"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
from array_queue import ArrayQueue
from process import Process
class QueueManager:
    def __init__(self, cola_registro: ArrayQueue[Process]):

        self._cola_registro = cola_registro

    def management(self):
        cola_gpu_short = ArrayQueue()
        cola_gpu_long = ArrayQueue()
        cola_cpu_short = ArrayQueue()
        cola_cpu_long = ArrayQueue()

        for proceso in self.cola_registro:

            if proceso.resource_type == "gpu" and proceso.execution_time == "short":
                cola_gpu_short.enqueue(proceso)
            elif proceso.resource_type == "gpu" and proceso.execution_time == "long":
                cola_gpu_long.enqueue(proceso)
            elif proceso.resource_type == "cpu" and proceso.execution_time == "short":
                cola_cpu_short.enqueue(proceso)
            elif proceso.resource_type == "cpu" and proceso.execution_time == "long":
                cola_cpu_long.enqueue(proceso)
            else:
                print("supererror slaynt sach")
       