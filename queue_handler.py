"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
from array_queue import ArrayQueue
from process import Process
class Usuario:
    def __init__(self, id_usuario, penalizacion):
        self.id_usuario = id_usuario
        self.penalizacion = penalizacion

    def reducir_penalizacion(self):
        self.penalizacion -= 1
        if self.penalizacion < 0:
            self.penalizacion = 0

    def aumentar_penalizacion(self):
        self.penalizacion += 5

    def __repr__(self):
        return f"Usuario({self.id_usuario}, {self.penalizacion})"

class ProcessManager:
    def __init__(self, cola_registro: ArrayQueue[Process], time):

        self._cola_registro = cola_registro
        

    def elegir_colas(self, cola_registro):
        """Según los datos de cada proceso lo asigna a una cola o otra."""
        cola_gpu_short = ArrayQueue()
        cola_gpu_long = ArrayQueue()
        cola_cpu_short = ArrayQueue()
        cola_cpu_long = ArrayQueue()

        for proceso in self.cola_registro:

            if proceso.resource_type == "gpu" and proceso.execution_time == "short":
                cola_registro.dequeue(proceso)
                cola_gpu_short.enqueue(proceso)
                
            elif proceso.resource_type == "gpu" and proceso.execution_time == "long":
                cola_registro.dequeue(proceso)
                cola_gpu_long.enqueue(proceso)

            elif proceso.resource_type == "cpu" and proceso.execution_time == "short":
                cola_registro.dequeue(proceso)
                cola_cpu_short.enqueue(proceso)

            elif proceso.resource_type == "cpu" and proceso.execution_time == "long":
                cola_registro.dequeue(proceso)
                cola_cpu_long.enqueue(proceso)

            else:
                print("supererror slaynt sach")
                
    def ejecucion(self, cola_gpu_short,cola_gpu_long, cola_cpu_short,cola_cpu_long):
        cola_ejecucion = ArrayQueue()
        time = 0 #eso mejor bucle akdana
        for proceso in cola_gpu_short:
            pass

    def agregar_proceso_ejecucion(self, proceso_a_añadir,cola_ejecucion,time):
        """Comprueba que no haya ningún proceso de su misma cola, y si no hay, o este ya cumplió su tiempo añade el nuevo"""

        subcola = f"cola_{proceso_a_añadir.resource_type}_{proceso_a_añadir.execution_time}"

        cola_revisada = ArrayQueue()
        for proceso in cola_ejecucion:

            subcola2 = f"cola_{proceso.resource_type}_{proceso.execution_time}"


            if subcola == subcola2 and (time - proceso.start_time) == proceso.execution_time: 
                cola_ejecucion.dequeue(proceso)
                cola_ejecucion.enqueue(proceso_a_añadir)
                print(f"Añadido un nuevo proceso de la subcola: {subcola}.")
                
            
            else: 
                cola_revisada.enqueue(proceso)
        cola_ejecucion = cola_revisada
        
        return cola_ejecucion
        

    def remover_proceso_ejecucion(self, proceso):
        subcola = f"cola_{proceso.resource_type}_{proceso.execution_time}"
        if subcola in self.cola_procesos_en_ejecucion and self.cola_procesos_en_ejecucion[subcola] == proceso:
            del self.cola_procesos_en_ejecucion[subcola]
            return True
        else:
            print(f"El proceso {proceso} no está en ejecución.")
            return False
             



    def usuario_penalizado(self,id_usuario):
        usuario_en_cola = None

        for usuario in self.cola_usuarios_penalizados:
            if usuario.id_usuario == id_usuario:
                usuario_en_cola = usuario
                return True
            else:
                return False

    def añadir_usuario_cola(self, id_usuario):
        """Revisa si un usuario está en la cola de penalizados, si ya está, le añade 5 ud de tiempo a la penalización, si no simplemente lo añade con penalización 5
        """
        usuario_en_cola = None

        for usuario in self.cola_usuarios_penalizados:
            if usuario.id_usuario == id_usuario:
                usuario_en_cola = usuario
                break

        if usuario_en_cola:
            usuario_en_cola.aumentar_penalizacion()

        else:
            nuevo_usuario = Usuario(id_usuario, 5)
            self.cola_usuarios_penalizados.append(nuevo_usuario)

    def control_penalizacion_usuarios(self, cola_usuarios_penalizados):
        """Revisa todos los usuarios y elimina aquellos que ya cumplieron su penalizacióm, para los demás les resta una ud de tiempo a su penalizacion"""

        cola_penalizados_revisada = ArrayQueue()

        for usuario in cola_usuarios_penalizados:

            usuario.reducir_penalizacion

            if usuario.penalizacion == 0:
                pass

            else:
                cola_penalizados_revisada.enqueue(usuario)

        cola_usuarios_penalizados = cola_penalizados_revisada

        return cola_usuarios_penalizados 







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
