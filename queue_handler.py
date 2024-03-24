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
    def __init__(self, cola_registro: ArrayQueue[Process], cola_ejecucion):

        self._cola_registro = cola_registro
        self._cola_ejecucion = cola_ejecucion
        

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
                
    def ejecucion(self, cola_registro, cola_ejecucion, cola_gpu_short, cola_gpu_long, cola_cpu_short, cola_cpu_long):
        cola_ejecucion = ArrayQueue()
        time = 0 #eso mejor bucle akdana
        while not cola_ejecucion.is_empty() and not (cola_gpu_short.is_empty() or cola_gpu_long.is_empty() or cola_cpu_short.is_empty() or cola_cpu_long.is_empty()) and not cola_registro.is_empty()
            time+=1
            

    def agregar_proceso_ejecucion(self, proceso_a_añadir, cola_ejecucion,time):
        """Comprueba que no haya ningún proceso de su misma cola, y si no hay, o este ya cumplió su tiempo añade el nuevo"""

        subcola = f"cola_{proceso_a_añadir.resource_type}_{proceso_a_añadir.execution_time}"

        cola_revisada = ArrayQueue()
        for proceso in cola_ejecucion:

            subcola2 = f"cola_{proceso.resource_type}_{proceso.execution_time}"


            if (subcola == subcola2) and ((time - proceso.start_time) == proceso.execution_time): 
                cola_ejecucion.dequeue(proceso)
                print(f"El proceso existente de la sunbcola {subcola} ha finalizado su ejecución")
                cola_ejecucion.enqueue(proceso_a_añadir)
                print(f"Añadido un nuevo proceso de la subcola: {subcola}.")
                
            
            else: 
                cola_revisada.enqueue(proceso)

        cola_ejecucion = cola_revisada
        
        return cola_ejecucion

    def usuario_penalizado(self,id_usuario):
        usuario_en_cola = None

        for usuario in self.cola_usuarios_penalizados:
            if usuario.id_usuario == id_usuario:
                usuario_en_cola = usuario
                return True
            else:
                return False

    def añadir_usuario_cola(self, id_usuario):
        """
        Revisa si un usuario está en la cola de penalizados, si ya está, le añade 5 ud de tiempo a la penalización, si no simplemente lo añade con penalización 5
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
        """
        Revisa todos los usuarios y elimina aquellos que ya cumplieron su penalizacióm, para los demás les resta una ud de tiempo a su penalizacion.
        """

        cola_penalizados_revisada = ArrayQueue()

        for usuario in cola_usuarios_penalizados:

            usuario.reducir_penalizacion

            if usuario.penalizacion == 0:
                pass

            else:
                cola_penalizados_revisada.enqueue(usuario)

        cola_usuarios_penalizados = cola_penalizados_revisada

        return cola_usuarios_penalizados 

 