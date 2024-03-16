"""
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
Claudia Vidal Otero (claudia.votero@udc.es)
"""
import time

class Process:
    def __init__(self, pid, user_id, resource_type, execution_time, start_time):
        """
        Inicializa la clase Process y se le asignan sus atributos.

        Parameters:
            pid
            user_id
            resource_type
            execution_time
            start_time
        """
        self._pid = pid
        self._user_id = user_id
        self._resource_type = resource_type
        self._execution_time = execution_time
        self._start_time = start_time

    @property
    def pid(self):
        # Property (getter) para pid
        return self._pid
    @pid.setter
    def pid(self, value):
        # Setter para pid
        self._pid = value
    
    @property
    def user_id(self):
        # Property (getter) para user_id
        return self._user_id
    @user_id.setter
    def user_id(self, value):
        # Setter para user_id
        self._user_id = value

    @property
    def resource_type(self):
        # Property (getter) para resource_type
        return self._resource_type
    @resource_type.setter
    def resource_type(self, value):
        # Setter para resource_type
        self._resource_type = value

    @property
    def execution_time(self):
        # Property (getter) para execution_time
        return self._execution_time
    @execution_time.setter
    def execution_time(self, value):
        # Setter para execution_time
        self._execution_time = value
    
    @property
    def start_time(self):
        # Property (getter) para start_time
        return self._start_time
    @start_time.setter
    def start_time(self, value):
        # Setter para start_time
        self._start_time = value
    
