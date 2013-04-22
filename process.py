import time
import multiprocessing as mp
from controller import *


# from datetime import *

class Proceso:

    def __init__( self, id, nombre, tipo, prioridad, duracion):
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = priority
        # self.date = datetime.today()
        self.length = duracion
        self.time_left = duracion

    def getType(self):
        return self.type

    def getTime_left(self):
        return self.time_left

    def getDate(self):
        return self.date

    def getPriority(self):
        return self.priority

    def getName(self):
        return self.name

    def getLength(self):
        return self.length

    def getId(self):
        return self.id

class Llamada(Proceso):

    def __init__(self, nombre, tipo, prioridad, numero, duracion):
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        # self.date = datetime.today()
        self.time = int(duracion)
        self.time_left = int(duracion)
        self.number = numero
        

    def getNumber(self):
        return self.number 

    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        print self.name + str(self.time_left)

        if self.type=='1':
            print "LLamando a: ", self.number
            if( self.time_left == 0):     #Proceso termino
                return True
            else:
                return False

        if self.type=='2':
            print "Recibiendo llamada de: ", self.number
            if( self.time_left == 0):     #Proceso termino
                return True
            else:
                return False


class Mensaje(Proceso):

    def __init__(self, nombre, tipo, prioridad, numero,texto):
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        self.time = len(texto)
        self.time_left = self.time
        self.number = numero
        self.text = texto

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text
        
    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        print self.name + str(self.time_left)

        if self.type=='3':
            # print "Enviando mensaje a: ", self.number
            if( self.time_left == 0):     #Proceso termino
                return True
            else:
                return False

        if self.type=='4':
            # print "Recibiendo mensaje de: ", self.number
            if( self.time_left == 0):     #Proceso termino
                return True
            else:
                return False


           
        
        





