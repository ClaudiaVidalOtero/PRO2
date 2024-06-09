"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""

class Proceso:
    def __init__(self, pid, id_usuario, tipo_recurso, tiempo_estimado, tiempo_ejecucion):
        """
        Inicializa la clase Process y se le asignan sus atributos.

        Parameters:
            pid (str): Identificador del proceso.
            id_usuario (str): Identificador del usuario.
            tipo_recurso (str): Tipo de recurso (cpu / gpu).
            tiempo_estimado (str): Tiempo estimado de ejecución (long / short).
            tiempo_ejecucion (int): Tiempo de inicio de ejecución.
        """
        self._pid = pid
        self._id_usuario = id_usuario
        self._tipo_recurso = tipo_recurso
        self._tiempo_estimado = tiempo_estimado
        self._tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_entrada = None
        self.tiempo_inicio = None

    @property
    def pid(self):
        # Property (getter) para pid
        return self._pid
    @pid.setter
    def pid(self, value):
        # Setter para pid
        self._pid = value
    
    @property
    def id_usuario(self):
        # Property (getter) para id_usuario
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, value):
        # Setter para id_usuario
        self._id_usuario = value

    @property
    def tipo_recurso(self):
        # Property (getter) para tipo_recurso
        return self._tipo_recurso
    @tipo_recurso.setter
    def tipo_recurso(self, value):
        # Setter para tipo_recurso
        self._tipo_recurso = value

    @property
    def tiempo_estimado(self):
        #Property (getter) para estimated execution time
        return self._tiempo_estimado
    @tiempo_estimado.setter
    def tiempo_estimado(self, value):
        #setter para tiempo_estimado
        self._tiempo_estimado = value

    @property
    def tiempo_ejecucion(self):
        # Property (getter) para tiempo_ejecucion
        return self._tiempo_ejecucion
    @tiempo_ejecucion.setter
    def tiempo_ejecucion(self, value):
        # Setter para tiempo_ejecucion
        self._tiempo_ejecucion = value
    