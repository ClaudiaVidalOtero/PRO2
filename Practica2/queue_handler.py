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


    def __repr__(self):
        return f"Usuario({self.id_usuario}, {self.penalizacion})"

