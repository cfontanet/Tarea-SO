from multiprocessing import Process 
import time
import os 
from tarea1 import *

class Proceso:

    def __init__(self,id,nombre,tiempo):
        self.id = id
        self.name = nombre
        self.time = tiempo

    def getName(self):
        return self.name

    def getTime(self):
        return self.time

    def getId(self):
        return self.id

class Llamada(Proceso):

    def __init__(self,nombre,tiempo,numero,duracion):
        self.id = id
        self.name = nombre
        self.time = tiempo
        self.number = numero
        self.length = duracion

    def getNumber(self):
        return self.number

    def getLength(self):
        return self.length

class Mensaje(Proceso):

    def __init__(self,nombre,numero,texto):
        self.id = id
        self.name = nombre
	    
        self.time =len(texto)
        self.text = texto

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text
    def correr(self):
	time.sleep(self.time)
        print self.text



if __name__ == '__main__':
    
    	a=Mensaje("blas",0,"h")
    	#b=Mensaje("ohf",0,"hol")
    	#c=Mensaje("qwer",0,"hola")
    	p1= Process(target=a.correr())
	   #time.sleep(1)
    	#p2= Process(target=b.correr())
	   #time.sleep(2)	
	   #p3= Process(target=c.correr())    	
	   #p1.start()
    	p1.join()
        print heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 0, 1, 2, 3, 4, 5, 6, 7])
  
