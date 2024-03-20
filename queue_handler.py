"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
from array_queue import ArrayQueue
from process import Process
class ProcessManager:
    def __init__(self, cola_registro: ArrayQueue[Process], time):

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
                
    def ejecucion(self, cola_gpu_short,cola_gpu_long, cola_cpu_short,cola_cpu_long):
        for proceso in cola_gpu_short:
            pass

    def penalizar_usuario(self, tiempo_actual, id_usuario):
        cola_usuarios_penalizados = ArrayQueue()

        if id_usuario is not cola_usuarios_penalizados():         
            cola_usuarios_penalizados.enqueue([tiempo_actual,id_usuario])
        else:
            cola_usuarios_penalizados.dequeue(el usuario )
            cola_usuarios_penalizados.enqueue([tiempo_actual,id_usuario])
        

        print(f"Penalización activa: {tiempo_actual} {id_usuario}")






class GestorColas:
    def __init__(self):
        self.cpu_short = ColaEjecucion()
        self.cpu_long = ColaEjecucion()
        self.gpu_short = ColaEjecucion()
        self.gpu_long = ColaEjecucion()
        self.procesos_en_ejecucion = {}

    def agregar_proceso(self, proceso):
        if proceso.tipo == 'cpu':
            if proceso.tiempo_estimado == 'short':
                self.cpu_short.agregar_proceso(proceso)
            else:
                self.cpu_long.agregar_proceso(proceso)
        else:
            if proceso.tiempo_estimado == 'short':
                self.gpu_short.agregar_proceso(proceso)
            else:
                self.gpu_long.agregar_proceso(proceso)

    def ejecutar_procesos(self, tiempo_actual):
        procesos_terminados = []
        for tipo_cola in [self.cpu_short, self.cpu_long, self.gpu_short, self.gpu_long]:
            if tipo_cola.obtener_proceso() is not None:
                proceso = tipo_cola.obtener_proceso()
                if proceso.id_usuario in self.procesos_en_ejecucion:
                    if tiempo_actual >= self.procesos_en_ejecucion[proceso.id_usuario]['t_inicio_ejecucion'] + proceso.tiempo_ejecucion:
                        procesos_terminados.append(proceso)
                        del self.procesos_en_ejecucion[proceso.id_usuario]
                else:
                    proceso.tiempo_inicio_ejecucion = tiempo_actual
                    self.procesos_en_ejecucion[proceso.id_usuario] = {'t_inicio_ejecucion': tiempo_actual, 'tipo_cola': tipo_cola}

        for proceso in procesos_terminados:
            print(f"Proceso terminado: {tiempo_actual} {proceso.id_proceso} {proceso.id_usuario} {proceso.tipo} {proceso.tiempo_estimado} {proceso.tiempo_entrada} {proceso.tiempo_inicio_ejecucion} {proceso.tiempo_ejecucion}")
            if proceso.tiempo_estimado == 'short' and proceso.tiempo_ejecucion > 5:
                print(f"Penalización aplicada: {tiempo_actual} {proceso.id_proceso} {proceso.id_usuario}")
            del proceso

    def penalizar_usuario(self, tiempo_actual, id_usuario):
        cola_usuarios_penalizados = ArrayQueue()

        if id_usuario is not cola_usuarios_penalizados():         
            cola_usuarios_penalizados.enqueue([tiempo_actual,id_usuario])
        else:
            cola_usuarios_penalizados.dequeue(el usuario )
            cola_usuarios_penalizados.enqueue([tiempo_actual,id_usuario])
        

        print(f"Penalización activa: {tiempo_actual} {id_usuario}")
