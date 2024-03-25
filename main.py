"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import sys
from array_queue import ArrayQueue
from process import Process
from queue_handler import Usuario

class QueueSimulator:
    def create_cola_registro(self, text: str):
        cola_registro = ArrayQueue()
        lines = text.split("\n")

        for line in lines:
            parts = line.split()  # Dividir la línea en partes separadas por espacios
            if len(parts) == 5:  # Asegurarse de que haya 5 partes en la línea
                # Extraer los atributos del proceso
                pid = parts[0]
                user_id = parts[1]
                resource_type = parts[2]
                estimated_execution_time = parts[3]
                execution_time = int(parts[4])
                start_time = None

                # Crear un proceso y agregarlo a la cola de registro
                proceso = Process(pid, user_id, resource_type, estimated_execution_time, execution_time, start_time)
                cola_registro.enqueue(proceso)
        return cola_registro
        
class ProcessManager:

    def ejecucion(self, cola_registro):
        cola_ejecucion = ArrayQueue()

        cola_finalizados = ArrayQueue()

        cola_usuarios_penalizados = ArrayQueue()

        cola_gpu_short = ArrayQueue()
        cola_gpu_long = ArrayQueue()
        cola_cpu_short = ArrayQueue()
        cola_cpu_long = ArrayQueue()

        time = 1 
        print("pan")
        #while not cola_registro.is_empty():
        #    proceso = cola_registro.first()
        #    print(proceso.pid, proceso.user_id, proceso.resource_type, proceso.estimated_execution_time, proceso.execution_time, proceso.start_time)
        #    cola_registro.dequeue()
            
        while not (cola_registro.is_empty() and cola_ejecucion.is_empty() and cola_cpu_long.is_empty() and cola_cpu_short.is_empty() and cola_gpu_long.is_empty() and cola_gpu_short.is_empty()):
        # Tu código aquí

            proceso = cola_registro.first()

            if proceso.resource_type == "gpu" and proceso.estimated_execution_time == "short":
                print("pan")
                cola_registro.dequeue()
                cola_gpu_short.enqueue(proceso)
                print("pan")
                
            elif proceso.resource_type == "gpu" and proceso.estimated_execution_time == "long":
                cola_registro.dequeue()
                cola_gpu_long.enqueue(proceso)

            elif proceso.resource_type == "cpu" and proceso.estimated_execution_time == "short":
                cola_registro.dequeue()
                cola_cpu_short.enqueue(proceso)

            elif proceso.resource_type == "cpu" and proceso.estimated_execution_time == "long":
                cola_registro.dequeue()
                cola_cpu_long.enqueue(proceso)

            else:
                print("supererror slaynt sach")

            if not self.usuario_penalizado(proceso.user_id, cola_usuarios_penalizados):
                print("pan")
                self.agregar_proceso_ejecucion(proceso,cola_ejecucion, cola_finalizados, cola_usuarios_penalizados, time)
            else:
                subcola = f"cola_{proceso.resource_type}_{proceso.estimated_execution_time}"
                subcola.enqueue(proceso)
            self.control_penalizacion_usuarios(cola_usuarios_penalizados)
            time += 1

            
            
            

    def agregar_proceso_ejecucion(self, proceso_a_añadir, cola_ejecucion, cola_finalizados,cola_usuarios_penalizados, time):
        """Comprueba que no haya ningún proceso de su misma cola, y si no hay, o este ya cumplió su tiempo añade el nuevo"""

        subcola = f"cola_{proceso_a_añadir.resource_type}_{proceso_a_añadir.estimated_execution_time}"
        proceso_a_añadir.start_time = time
        cola_revisada = ArrayQueue()
        for proceso in cola_ejecucion:

            subcola2 = f"cola_{proceso.resource_type}_{proceso.estimated_execution_time}"


            if (subcola == subcola2) and ((time - proceso.start_time) == proceso.estimated_execution_time): 
                cola_ejecucion.dequeue()
                cola_finalizados.enqueue(proceso)
                if proceso.estimated_execution_time == "short" and proceso.execution_time > 5:
                    self.añadir_usuario_cola(proceso.id_usuario, cola_usuarios_penalizados)
                else: 
                    pass
                print(f"El proceso existente de la subcola {subcola} ha finalizado su ejecución")
                cola_ejecucion.enqueue(proceso_a_añadir)
                print(f"Añadido un nuevo proceso de la subcola: {subcola}.")
                print(proceso_a_añadir.start_time)
                
            
            else: 
                cola_revisada.enqueue(proceso)

        cola_ejecucion = cola_revisada
        
        return cola_ejecucion

    def usuario_penalizado(self,id_usuario, cola_usuarios_penalizados):
        """Comprueba si un usuario está penalizado"""
        usuario_en_cola = None

        for usuario in cola_usuarios_penalizados:
            if usuario.id_usuario == id_usuario:
                usuario_en_cola = usuario
                return True
            else:
                return False

    def añadir_usuario_cola(self, id_usuario, cola_usuarios_penalizados):
        """
        Revisa si un usuario está en la cola de penalizados, si no simplemente lo añade con penalización 5
        """
        nuevo_usuario = Usuario(id_usuario, 5)
        cola_usuarios_penalizados.enqueue(nuevo_usuario)

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

 

def main():
    
    """
    La función principal que lee desde un archivo y comienza la simulación.
    """

    with open(sys.argv[1]) as f:
        process_text = f.read()
        lector_archivos = QueueSimulator()
        cola_registro = lector_archivos.create_cola_registro(process_text)
        simulator = ProcessManager()

        simulator.ejecucion(cola_registro)


if __name__ == "__main__":
    main()
    