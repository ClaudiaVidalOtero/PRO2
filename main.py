"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import sys
import pandas
from pokemon import *
from trainer import Trainer

<<<<<<< Updated upstream

class PokemonSimulator:
    
    """Una clase que simula entrenadores de Pokémon y sus Pokémon."""
    
    lista_datos_pokemon = [] # lista que almacena datos estadísticos de las batallas de Pokémon.

    def create_trainer_and_pokemons(self, text: str):
        
        """
        Crea un entrenador y sus Pokémon a partir de un texto dado como entrada.

        Parameters:
            text (str): Texto multilínea donde la primera línea es el nombre del entrenador y las líneas subsiguientes contienen detalles de los Pokémon.

        Returns:
            Instancia de Trainer.
        """

        lines = text.split("\n")
        trainer_name = lines[0]
        pokemons = []

        # Iterating over each pokemon line in the input
        for line in lines[1:]:
            parts = line.split(' (')
            pokemon_name = parts[0] # Extracting the pokemon's name
            details = parts[1].strip(')').split(', ')  # Splitting other attributes
            # Extracting and converting each attribute
            pokemon_type = details[0].split(': ')[1]
            level = int(details[1].split(': ')[1])
            strength = int(details[2].split(': ')[1])
            defense = int(details[3].split(': ')[1])
            hp = int(details[4].split(': ')[1])
            total_hp = hp # Setting total_hp equal to the initial hp
            agility = int(details[5].split(': ')[1])
            
            # Creating pokemons based on their type
            if pokemon_type == 'Fire':
                temperature = float(details[6].split(': ')[1])
                pokemon_instance = FirePokemon(name=pokemon_name, level=level, strength=strength,
                                               defense=defense, hp=hp, total_hp=total_hp,
                                               agility=agility, pokemon_type=pokemon_type, temperature=temperature)
            elif pokemon_type == 'Grass':
                healing = float(details[6].split(': ')[1])
                pokemon_instance = GrassPokemon(name=pokemon_name, level=level, strength=strength,
                                                defense=defense, hp=hp, total_hp=total_hp,
                                                agility=agility, pokemon_type=pokemon_type, healing=healing)
            elif pokemon_type == 'Water':
                surge_mode = False
                pokemon_instance = WaterPokemon(name=pokemon_name, level=level, strength=strength,
                                                defense=defense, hp=hp, total_hp=total_hp,
                                                agility=agility, pokemon_type=pokemon_type, surge_mode=surge_mode)
            else: 
                raise ValueError(f"Invalid Pokemon type: {pokemon_type}")
            
            pokemons.append(pokemon_instance)

        # Create an instance of Trainer with the created Pokemon
        trainer_instance = Trainer(name=trainer_name, pokemon=pokemons)

        return trainer_instance

    def parse_file(self, text: str):
        """
        Analiza el texto proporcionado para crear entrenadores y sus Pokémon.

        Parameters:
            text (str): El texto completo que se va a analizar, representando dos entrenadores y sus Pokémon.

        Returns:
            Las instancias de Trainer para los dos entrenadores.
        """

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return trainer1, trainer2
    
    def attack(self, round_number, attacker, defender):    
        """
        Realiza un ataque entre un atacante y un defensor Pokémon.

        Parameters:
            round_number (int): Número de ronda del juego.
            attacker (Pokemon): El Pokémon atacante.
            defender (Pokemon): El Pokémon defensor.

        """  
        if int(round_number) % 2 != 0 and not defender.is_debilitated():
            #Si estamos en ronda impar los Pokémon usarán sus habilidades especiales.

            if attacker.pokemon_type == "Grass":
                #Si es tipo grass, realizará grass_attack y luego curación.
                type_attack = "grass_attack"
                damage = getattr(attacker, type_attack)(defender)
                print(f"-{attacker.name} uses a {type_attack} on {defender.name}! (Damage: -{damage} HP: {defender.hp})")

                gained_healing = attacker.heal()
                #Guardamos sus datos en instancias de la clase Estadística para luego crear el dataframe.
                self.lista_datos_pokemon.append(Estadistica(attacker.pokemon_type, attacker.name, damage, defender.pokemon_type, gained_healing))
                print(f"-{attacker.name} is healing! (Healing: +{gained_healing} HP: {attacker.hp})")
                            

            elif attacker.pokemon_type == "Fire":
                #Si es tipo fire, realizará fire_attack y luego embers.
                type_attack = "fire_attack"
                damage = getattr(attacker, type_attack)(defender)
                print(f"-{attacker.name} uses a {type_attack} on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                
                damage_embers = attacker.embers(defender)

                #Guardamos sus datos en instancias de la clase Estadística para luego crear el dataframe.
                self.lista_datos_pokemon.append(Estadistica(attacker.pokemon_type, attacker.name, (damage + damage_embers), defender.pokemon_type, 0 ))
                
                print(f"-{attacker.name} uses embers on {defender.name}! (Damage: -{damage_embers} HP: {defender.hp})")
            
            elif attacker.pokemon_type == "Water":
                #Si es tipo Water, realizará water_attack.
                type_attack = "water_attack"
                damage = getattr(attacker, type_attack)(defender)

                #Guardamos sus datos en instancias de la clase Estadística para luego crear el dataframe.
                self.lista_datos_pokemon.append(Estadistica(attacker.pokemon_type, attacker.name, damage, defender.pokemon_type, 0 ))

                print(f"-{attacker.name} uses a {type_attack} on {defender.name}! (Damage: -{damage} HP: {defender.hp})")
                
        else:
            #Si no estamos en ronda impar el atacante sólo hará un ataque básico.
            type_attack = "basic_attack"
            damage = getattr(attacker, type_attack)(defender)

            #Guardamos sus datos en instancias de la clase Estadística para luego crear el dataframe.
            self.lista_datos_pokemon.append(Estadistica(attacker.pokemon_type, attacker.name, damage, defender.pokemon_type, 0 ))
            
            print(f"-{attacker.name} uses a {type_attack} on {defender.name}! (Damage: -{damage} HP: {defender.hp})")        
                  
    def print_round_info(self, round_number, p1, p2):
        """
        Imprime la información de la ronda en un juego de combate.

        Parameters:
            round_number (int): Número de la ronda.
            p1 (str): Información del luchador 1.
            p2 (str): Información del luchador 2.
        """
        print(f"┌───────── Round {round_number} ─────────┐")
        print(f"Fighter 1: {p1}")
        print(f"Fighter 2: {p2}")
        print("Actions") 

    def battle(self, trainer1, trainer2):
        """
        Simula una batalla entre dos entrenadores de Pokémon.

        Parameters:
            trainer1 (Trainer): El primer entrenador.
            trainer2 (Trainer): El segundo entrenador.
        """
        p1 = trainer1.select_first_pokemon()
        p2 = trainer2.select_first_pokemon()

        self.print_battle_start(trainer1, trainer2, p1, p2)

        round_number = 1
        while not p1.is_debilitated() and not p2.is_debilitated():
            attacker, defender = self.determine_attack_order(p1, p2)
            self.execute_round(round_number, attacker, defender)
            round_number += 1

            if p1.is_debilitated():
                self.handle_debilitated_pokemon(trainer1, trainer2, p1, p2)
                p1 = trainer1.selected_pokemon
                round_number = 1
            elif p2.is_debilitated():
                self.handle_debilitated_pokemon(trainer2, trainer1, p2, p1)
                p2 = trainer2.selected_pokemon
                round_number = 1

    def print_battle_start(self, trainer1, trainer2, p1, p2):
        """
        Imprime un mensaje indicativo al inicio de la batalla.

        Parameters:
            trainer1 (Trainer): El primer entrenador.
            trainer2 (Trainer): El segundo entrenador.
            p1 (Pokemon): El Pokémon seleccionado por el primer entrenador.
            p2 (Pokemon): El Pokémon seleccionado por el segundo entrenador.
        """
        print("=================================")
        print(f"Battle between: {trainer1.name} vs {trainer2.name} begins!")
        print(f"{trainer1.name} chooses {p1.name}")
        print(f"{trainer2.name} chooses {p2.name}")
        print("=================================")
    
    def determine_attack_order(self, pokemon1, pokemon2):
        """
        Determina el orden de ataque basado en la agilidad de los Pokémon.

        Parameters:
            pokemon1 (Pokemon): El Pokémon del trainer1.
            pokemon2 (Pokemon): El Pokémon del trainer2.
        Returns:
            Instancias del atacante y el defensor.

        """
        if pokemon1.agility >= pokemon2.agility:
            attacker = pokemon1
            defender = pokemon2
        else:
            attacker = pokemon2
            defender = pokemon1

        return attacker, defender

    def execute_round(self, round_number, attacker, defender):
        """
        Ejecuta una ronda de la batalla, mostrando información de los Pokémon luchadores, 
        realizando ataques y manejando debilitaciones.

        Parameters:
            round_number (int): El número de la ronda actual.
            attacker (Pokemon): El Pokémon atacante.
            defender (Pokemon): El Pokémon defensor.
        """
        self.print_round_info(round_number, attacker, defender)
        self.attack(round_number, attacker, defender)
        if defender.is_debilitated():
            print(f"{defender.name} is debilitated")
        else:
            self.attack(round_number, defender, attacker)
            if attacker.is_debilitated():
                print(f"{attacker.name} is debilitated")

    def handle_debilitated_pokemon(self, losing_trainer, winning_trainer, debilitated_pokemon, opponent):
        """
        Maneja la situación en la que un Pokémon se debilita durante la batalla.
    
        Si el entrenador cuyo Pokémon se debilita tiene más Pokémon disponibles, selecciona el siguiente Pokémon
        para continuar la batalla. De lo contrario, declara al otro entrenador como el ganador de la batalla.

        Parameters:
            losing_trainer (Trainer): El entrenador cuyo Pokémon se ha debilitado.
            winning_trainer (Trainer): El entrenador que ha ganado la batalla.
            debilitated_pokemon (Pokemon): El Pokémon debilitado.
            opponent (Pokemon): El Pokémon del oponente.
        """
        selected_pokemon = losing_trainer.select_next_pokemon(opponent)
        if selected_pokemon is not None:
            print(f"{losing_trainer.name} chooses {selected_pokemon.name}")
            losing_trainer.selected_pokemon = selected_pokemon
        else:
            print("=================================")
            print(f"End of the Battle: {winning_trainer.name} wins!")
            print("=================================")
    
class Estadistica:
    """
    Clase para representar estadísticas de un pokémon en combate.

    Parameters:
        p_type (str): Tipo del personaje.
        name (str): Nombre del personaje.
        damage (int): Daño que el personaje infringió en su ronda.
        opponent_type (str): Tipo de oponente contra el que el pokemon se enfrenta.
        gained_healing (int): Cantidad de curación que el personaje realiza en su ronda.
    """
    def __init__(self, p_type:str, name:str, damage:int, opponent_type:str, gained_healing:int):
        self._p_type = p_type
        self._name = name
        self._damage = damage
        self._opponent_type = opponent_type
        self._gained_healing = gained_healing 
    @property
    def name(self):
        # Property (getter) para name
        return self._name

    @property
    def p_type(self):
        # Property (getter) para tipo pokemon
        return self._p_type    
    @p_type.setter
    def p_type(self, value):
        # Setter para level
        self._p_type = value

    @property
    def damage(self):
        # Property (getter) para strength
        return self._damage
    @damage.setter
    def damage(self, value):
        # Setter para strength
        self._damage = value

    @property
    def opponent_type(self):
        # Property (getter) para strength
        return self._opponent_type
    @opponent_type.setter
    def strength(self, value):
        # Setter para strength
        self._opponent_type = value
    
    @property
    def gained_healing(self):
        # Property (getter) para strength
        return self._gained_healing
    @gained_healing.setter
    def gained_healing(self, value):
        # Setter para strength
        self._gained_healing = value

def estadisticas(self):
    #CREAMOS UN DATAFRAME CON LOS DATOS DE CADA RONDA.
    data = pandas.DataFrame([
        {"name": estadistica._name, "type": estadistica._p_type, "damage": estadistica._damage, 
         "opponent_type": estadistica._opponent_type, "healing": estadistica._gained_healing}
    for estadistica in self.lista_datos_pokemon ])
    print(data)


    #ESTADÍSTICAS DE LA SIMULACIÓN USANDO PANDAS
    
    #(1) El daño promedio causado por cada Pokémon individualmente.
    group_col = "name"
    target_col = "damage"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})
=======
class QueueSimulator:
    def __init__(self):
        self.cola_registro = None
        self.process_manager = ProcessManager()
        self.current_time = 0  # Inicializar el contador de tiempo aquí

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
    
    def execute_simulation(self, text: str):
        self.cola_registro = self.create_cola_registro(text)
        while not self.is_simulation_finished():
            self.current_time += 1

            if not self.cola_registro.is_empty():
                self.add_process_to_queue()

            self.process_manager.execute_running_processes(self.current_time)

    def is_simulation_finished(self):
        return self.cola_registro.is_empty() and self.process_manager.are_queues_empty()

    def add_process_to_queue(self):
        process = self.cola_registro.first()
        process.start_time = self.current_time
        self.process_manager.execute_process(process)
        self.cola_registro.dequeue()
        print(f"Proceso añadido a cola de ejecución: {self.current_time} {process.pid} {process.user_id} {process.resource_type} {process.estimated_execution_time}")
    
class ProcessManager:
    def __init__(self):
        self.cola_ejecucion = ArrayQueue()
        self.cola_finalizados = ArrayQueue()
        self.cola_usuarios_penalizados = ArrayQueue()
        self.cola_gpu_short = ArrayQueue()
        self.cola_gpu_long = ArrayQueue()
        self.cola_cpu_short = ArrayQueue()
        self.cola_cpu_long = ArrayQueue()
        self.usuarios_penalizados = set()  # Conjunto para rastrear usuarios penalizados

    def execute_running_processes(self, current_time):  # Aceptar current_time como parámetro
        while not self.cola_ejecucion.is_empty() or not self.cola_gpu_short.is_empty() or not self.cola_gpu_long.is_empty() \
                or not self.cola_cpu_short.is_empty() or not self.cola_cpu_long.is_empty():
            self.process_next(current_time)  # Pasar current_time a process_next

    def process_next(self, current_time):
        while not all(queue.is_empty() for queue in [self.cola_cpu_short, self.cola_cpu_long, self.cola_gpu_short, self.cola_gpu_long, self.cola_ejecucion]):
            # Procesar elementos de la cola de CPU de corto plazo
            if not self.cola_cpu_short.is_empty():
                self.execute_process(self.cola_cpu_short.dequeue())

            # Procesar elementos de la cola de CPU de largo plazo
            elif not self.cola_cpu_long.is_empty():
                self.execute_process(self.cola_cpu_long.dequeue())

            # Procesar elementos de la cola de GPU de corto plazo
            elif not self.cola_gpu_short.is_empty():
                self.execute_process(self.cola_gpu_short.dequeue())

            # Procesar elementos de la cola de GPU de largo plazo
            elif not self.cola_gpu_long.is_empty():
                self.execute_process(self.cola_gpu_long.dequeue())

            # Si no hay procesos en las colas de CPU y GPU, pero hay procesos en ejecución
            else:
                process = self.cola_ejecucion.first()
                if current_time - process.start_time >= process.execution_time:
                    self.finish_process(self.cola_ejecucion.dequeue())
                else:
                    # Aquí podrías aplicar alguna lógica adicional si es necesario
                    # Por ejemplo, verificar si algún proceso debe ser penalizado
                    self.process_penalty(process, current_time)



    def execute_process(self, process):
        self.cola_ejecucion.enqueue(process)
        print(f"Iniciando ejecución del proceso {process.pid}")

    def finish_process(self, process):
        self.cola_finalizados.enqueue(process)
        print(f"Proceso terminado: {self.current_time} {process.pid} {process.user_id} {process.resource_type} {process.estimated_execution_time} {process.start_time} {process.execution_time}")

    def process_penalty(self, process, current_time):
        if process.estimated_execution_time == "short" and process.execution_time > 5:
            # Penalizar al usuario solo si el proceso es "short" y supera el tiempo estimado
            self.add_user_penalty(process.user_id)
            print(f"Penalización activa: {current_time} {process.user_id}")
        else:
            # Si no se cumple la condición, ejecutar el proceso normalmente
            self.execute_process(process)



    def add_user_penalty(self, user_id):
        if user_id not in self.usuarios_penalizados:
            nuevo_usuario = Usuario(user_id, 5)
            self.cola_usuarios_penalizados.enqueue(nuevo_usuario)
            self.usuarios_penalizados.add(user_id)
        else:
            usuario = self.cola_usuarios_penalizados.find_user(user_id)
            usuario.penalizacion += 5
            print(f"Debido al incumplimiento de las normas, la penalización del usuario {usuario.id_usuario} se ha incrementado a {usuario.penalizacion} ud de tiempo.")

    def are_queues_empty(self):
        return self.cola_ejecucion.is_empty() and self.cola_gpu_short.is_empty() and self.cola_gpu_long.is_empty() \
               and self.cola_cpu_short.is_empty() and self.cola_cpu_long.is_empty()
>>>>>>> Stashed changes

    print("\n")
    print ("DAMAGE GROUPED BY NAME")
    print (data_pokemon)


    #2) El daño promedio causado por los Pokémon de cada tipo (agua, fuego, planta)
    group_col = "type"
    target_col = "damage"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})
    
    print("\n")
    print ("DAMAGE GROUPED BY TYPE")
    print (data_pokemon)


    #(3) El daño promedio que cada tipo de Pokémon inflige a cada uno de los otros tipos.
    group_col = ["type","opponent_type"]
    target_col = "damage"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})

    print("\n")
    print ("DAMAGE GROUPED BY (TYPE, OPPONENT_TYPE) ")
    print (data_pokemon)


    #(4) La curación promedia realizada por cada Pokémon.
    group_col = "name"
    target_col = "healing"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})

    print("\n")
    print ("HEALING GROUPED BY NAME")
    print (data_pokemon)

    #(5) La curación promedia realizada por los Pokémon de cada tipo.
    group_col = "type"
    target_col = "healing"
    data_pokemon = data.groupby(group_col).agg({target_col :["mean","std"]})

    print("\n")
    print ("HEALING GROUPED BY TYPE")
    print (data_pokemon)
    print("\n")

def main():

    """
    La función principal que lee desde un archivo y comienza la simulación.
    """

    with open(sys.argv[1]) as f:
<<<<<<< Updated upstream
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)
        simulator.battle(trainer1, trainer2)
        estadisticas(simulator)

    
=======
        process_text = f.read()
        simulator = QueueSimulator()
        simulator.execute_simulation(process_text)
>>>>>>> Stashed changes

if __name__ == '__main__':
    main()
