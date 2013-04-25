import time
import multiprocessing as mp
from controller import *
from historial import *
from agenda import *


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
        self.mostrar=""

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

    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        # print "Haciendo cualquier cosa de: "
        if( self.time_left == 0):     #Proceso termino
            return True
        else:
            return False
    def imprimirMensaje(self):
        print self.mostrar


class Llamada(Proceso):

    def __init__(self, nombre, tipo, prioridad, numero, duracion):
        self.historial= Historial()
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        # self.date = datetime.today()
        self.time = int(duracion)
        self.time_left = int(duracion)
        self.number = numero
        self.mostrar=""
        if tipo=='1':
            self.mostrar="LLamando a: ", self.number
        if tipo=='2':
            self.mostrar="Recibiendo llamada de: ", self.number

        

    def getNumber(self):
        return self.number 

    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        if self.type=='1':
            
            #print "LLamando a: ", self.number
            if( self.time_left == 0):     #Proceso termino
                self.historial.agregar_llamada('para', self.number)
                return True
            else:
                return False

        if self.type=='2':
            #print "Recibiendo llamada de: ", self.number
            if( self.time_left == 0):     #Proceso termino
                self.historial.agregar_llamada('de', self.number)
                return True
            else:
                return False


class Mensaje(Proceso):

    def __init__(self, nombre, tipo, prioridad, numero,texto):
        self.historial= Historial()
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        self.time = len(texto)
        self.time_left = self.time
        self.number = numero
        self.text = texto

        self.mostrar=""
        if tipo=='3':
            self.mostrar="Enviando Mensaje a: ", self.number
        if tipo=='4':
            self.mostrar="Recibiendo Mensaje de: ", self.number


    def getNumber(self):
        return self.number

    def getText(self):
        return self.text
        
    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        if self.type=='3':
            # print "Enviando mensaje a: ", self.number
            if( self.time_left == 0):     #Proceso termino
                self.historial.agregar_mensaje('para', self.number, self.text)
                return True
            else:
                return False

        if self.type=='4':
            # print "Recibiendo mensaje de: ", self.number
            if( self.time_left == 0):     #Proceso termino
                self.historial.agregar_mensaje('de', self.number, self.text)
                return True
            else:
                return False

class Contacto(Proceso):

    def __init__(self, nombre, tipo, prioridad, nombre_contacto, numero):
        self.agenda=Agenda()
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        self.time = 1
        self.time_left = self.time
        self.number = numero
        self.contact = nombre_contacto
        self.mostrar="Creando contacto"

    def getNumber(self):
        return self.number

    def getContact(self):
        return self.text
        
    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        # print "Recibiendo mensaje de: ", self.number
        if( self.time_left == 0):     #Proceso termino
            self.agenda.agregarContacto(self.contact, self.number)
            return True
        else:
            return False

class Cualquier(Proceso):

    def __init__(self, nombre, tipo, prioridad, duracion):
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        self.time = duracion
        self.time_left = self.time
        self.mostrar="Haciendo cualquier proceso"
        
    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        # print "Haciendo cualquier cosa de: "
        if( self.time_left == 0):     #Proceso termino
            return True
        else:
            return False

class Ubicacion(Proceso):

    def __init__(self, nombre, tipo, prioridad, duracion):
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        self.time = duracion
        self.time_left = self.time
        self.mostrar=""
        if tipo=='7':
            self.mostrar="Enviando Ubicacion"
        if tipo=='8':
            self.mostrar="Recibiendo Ubicacion"
        
    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        if self.type=='7':
            # print "Enviando mensaje a: ", self.number
            if( self.time_left == 0):     #Proceso termino
                return True
            else:
                return False

        if self.type=='8':
            # print "Recibiendo mensaje de: ", self.number
            if( self.time_left == 0):     #Proceso termino
                return True
            else:
                return False

class Jugar(Proceso):

    def __init__(self, nombre, tipo, prioridad, duracion):
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        self.time = duracion
        self.time_left = self.time
        self.mostrar="Jugando"

        
        
    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        # print "Haciendo cualquier cosa de: "
        if( self.time_left == 0):     #Proceso termino
            return True
        else:
            return False

class Musica(Proceso):

    def __init__(self, nombre, tipo, prioridad, duracion):
        self.id = id
        self.name = nombre
        self.type = tipo
        self.priority = prioridad
        self.time = duracion
        self.time_left = self.time
        self.mostrar= "Escuchando musica"
        
        
    def correr(self):
        time.sleep(1)
        self.time_left -= 1
        #print self.name + str(self.time_left)

        # print "Haciendo cualquier cosa de: "
        if( self.time_left == 0):     #Proceso termino
            return True
        else:
            return False
        





