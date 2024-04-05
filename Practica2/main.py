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
        print("Inicio Bucle")
            
        while not (cola_registro.is_empty() and cola_ejecucion.is_empty() and cola_cpu_long.is_empty() and cola_cpu_short.is_empty() and cola_gpu_long.is_empty() and cola_gpu_short.is_empty()):
            print("Entramos en el bucle")
            proceso = cola_registro.dequeue()
            if not cola_registro.is_empty():

                if proceso.resource_type == "gpu" and proceso.estimated_execution_time == "short":

                    print(f"GUARDAMOS EL ELEMENTO N:{time} del tipo {proceso.resource_type} y {proceso.estimated_execution_time}")
                    print(proceso)
                    cola_gpu_short.enqueue(proceso)

                    
                elif proceso.resource_type == "gpu" and proceso.estimated_execution_time == "long":

                    print(f"GUARDAMOS EL ELEMENTO N:{time} del tipo {proceso.resource_type} y {proceso.estimated_execution_time}")
                    print(proceso)
                    cola_gpu_long.enqueue(proceso)

                elif proceso.resource_type == "cpu" and proceso.estimated_execution_time == "short":

                    print(f"GUARDAMOS EL ELEMENTO N:{time} del tipo {proceso.resource_type} y {proceso.estimated_execution_time}")
                    print(proceso)
                    cola_cpu_short.enqueue(proceso)

                elif proceso.resource_type == "cpu" and proceso.estimated_execution_time == "long":

                    print(f"GUARDAMOS EL ELEMENTO N:{time} del tipo {proceso.resource_type} y {proceso.estimated_execution_time}")
                    print(proceso)
                    cola_cpu_long.enqueue(proceso)

                else:
                    print("supererror slaynt sach")

            print(f"Comprobamos que el usuario del proceso {time} no esté penalizado.")
            if not self.usuario_penalizado(proceso.user_id, cola_usuarios_penalizados):
                print(f"El usuario del proceso {time} no está penalizado.")
                cola_ejecucion = self.agregar_proceso_ejecucion(proceso, cola_ejecucion, cola_finalizados, cola_usuarios_penalizados, time)
            else:
                subcola = f"cola_{proceso.resource_type}_{proceso.estimated_execution_time}"
                print(f"El usuario del proceso {time} está penalizado.")
                !!!!!!!!!!!!!!!!!!!!!!!subcola.enqueue(proceso)
                print("Lo añadimos de vuelta a su subcola.")
            cola_usuarios_penalizados = self.control_penalizacion_usuarios(cola_usuarios_penalizados)
            time += 1
        print("Todas las colas están vacías.")
        return cola_finalizados

           
           
            

    def agregar_proceso_ejecucion(self, proceso_a_añadir, cola_ejecucion, cola_finalizados,cola_usuarios_penalizados, time):
        """Comprueba que no haya ningún proceso de su misma cola, y si no hay, o este ya cumplió su tiempo añade el nuevo"""

        subcola = f"cola_{proceso_a_añadir.resource_type}_{proceso_a_añadir.estimated_execution_time}"
        proceso_a_añadir.start_time = time
        coincidencias = False
        cola_revisada = ArrayQueue()
        print(f"Iniciamos el bucle de comprobar y agregar procesos para el proceso número: {time}")

        if cola_ejecucion.is_empty():
            print("La cola de ejecución está vacía.")
            cola_ejecucion.enqueue(proceso_a_añadir)

            print(f"Añadimos a la cola previamente vacía el proceso:{time}")

        else:

            while not cola_ejecucion.is_empty():
                print(f"Iniciamos el bucle que comprueba la existencia de procesos de subcolas para el proceso N:{time}")
                proceso = cola_ejecucion.dequeue()

                subcola2 = f"cola_{proceso.resource_type}_{proceso.estimated_execution_time}"

                if (subcola == subcola2) and ((time - proceso.start_time) == proceso.estimated_execution_time): 

                    cola_finalizados.enqueue(proceso)
                    coincidencias = True
                    cola_ejecucion.dequeue()
                    cola_revisada.enqueue(proceso_a_añadir)

                    print(f"El proceso existente de la subcola {subcola} ha finalizado su ejecución")
                    print(f"Añadido un nuevo proceso de la subcola: {subcola}, tiempo de inicio de ejecución: {proceso_a_añadir.start_time}.")

                    if proceso.estimated_execution_time == "short" and proceso.execution_time > 5:
                        self.añadir_usuario_cola(proceso.id_usuario, cola_usuarios_penalizados)

                elif subcola == subcola2:
                    coincidencias = True
                    pass
                
                else: 
                    cola_revisada.enqueue(proceso)
            cola_ejecucion = cola_revisada

            if not coincidencias:
                cola_revisada.enqueue(proceso_a_añadir)
            
        return cola_ejecucion

    def usuario_penalizado(self,id_usuario, cola_usuarios_penalizados):
        """Comprueba si un usuario está penalizado"""
        usuario_en_cola = None
        cola_revisada = ArrayQueue()

        while not cola_usuarios_penalizados.is_empty():
            usuario = cola_usuarios_penalizados.dequeue()
            if usuario.id_usuario == id_usuario:
                usuario_en_cola = usuario
                cola_revisada.enqueue(usuario)
                print(f"El usuario{usuario.id_usuario} no puede ejecutar procesos debido a su penalización, actualmente le quedan {usuario.penalizacion} unidades de tiempo.")
                return True
            else:
                cola_revisada.enqueue(usuario)
        cola_usuarios_penalizados = cola_revisada
        return False
    
    def añadir_usuario_cola(self, id_usuario, cola_usuarios_penalizados):
        """
        Revisa si un usuario está en la cola de penalizados, si no simplemente lo añade con penalización 5
        """
        nuevo_usuario = Usuario(id_usuario, 5)
        cola_usuarios_penalizados.enqueue(nuevo_usuario)
        print(f"Debido al incumplimiento de las normas, el usuario {nuevo_usuario.id_usuario} ha recibido una penalización de 5 ud de tiempo.")

    def control_penalizacion_usuarios(self, cola_usuarios_penalizados):
        """
        Revisa todos los usuarios y elimina aquellos que ya cumplieron su penalizacióm, para los demás les resta una ud de tiempo a su penalizacion.
        """

        cola_penalizados_revisada = ArrayQueue()
        if cola_usuarios_penalizados.is_empty():
            pass
        else:
            while not cola_usuarios_penalizados.is_empty():
                usuario = cola_usuarios_penalizados.dequeue()

                usuario.reducir_penalizacion

                if usuario.penalizacion == 0:
                    print(f"El usuario {usuario.id_usuario} ha finalizado su penalización y nuevamente puede ejecutar procesos.")
                    pass

                else:
                    cola_penalizados_revisada.enqueue(usuario)


        return cola_penalizados_revisada 

 

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
    