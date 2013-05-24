from heapq import *
import process as pr
from multiprocessing import *




class Controller:
    def __init__(self):
        self.h = []
        self.pactual = None

    def top(self):
        heap_aux = self.h
        print "\nNombre proceso \t \tPrioridad \t \tTiempo restante"
        
        if self.pactual:
            if len(self.pactual.getName()) >= 15:
                print self.pactual.getName(), "\t", self.pactual.getPriority(), "\t \t \t", self.pactual.getTime_left()
            else:
                print self.pactual.getName(), "\t \t", self.pactual.getPriority(), "\t \t \t", self.pactual.getTime_left()
        
        if heap_aux:
            for p in heap_aux:
                p_aux = p[1]
                if len(p_aux.getName()) >= 15:
                    print p_aux.getName(), "\t", p_aux.getPriority(), "\t \t \t", p_aux.getTime_left()
                else:
                    print p_aux.getName(), "\t \t", p_aux.getPriority(), "\t \t \t", p_aux.getTime_left()


    def simular(self, value, nombre):
        tiempo_actual = 0
        11
        entrantes = []

        if( nombre != ''):
            try:
                archivo = open( nombre, 'r', 0 )
                for line in archivo:
                    aux = line.strip().split( ';' )
                    entrantes.append( aux )

                archivo.close()
            except IOError:
                print "El archivo ", nombre ," no existe"


        while( True ):
            if (not value.empty()):
                aux1= value.get()
                
                if aux1=='top':
                    self.top()
                else:
                    heappush( self.h, ( aux1.getPriority(), aux1 ) )
                
            #Agrego los procesos que vienen entrando
            for p in entrantes:
                if( p[1] == str(tiempo_actual) ):
                    if( p[2] == '1' or p[2] == '2'):
                        aux = pr.Llamada( p[0], p[2], p[3], p[4], p[5] )

                    if( p[2] == '3' or p[2] == '4'):
                        aux = pr.Mensaje( p[0], p[2], p[3], p[4], p[5] )
                        
                    if( p[2] == '5'):
                        aux = pr.Contacto( p[0], p[2], p[3], p[4], p[5] )
                        
                    if( p[2] == '6'):
                        aux = pr.Cualquiera( p[0], p[2], p[3], p[4] )
                        
                    if( p[2] == '7'):
                        aux = pr.Ubicacion( p[0], p[2], p[3], 2 )
                        
                    if( p[2] == '8' ):
                        aux = pr.Ubicacion( p[0], p[2], p[3], p[4] )
                        
                    if( p[2] == '9'):
                        aux = pr.Jugar( p[0], p[2], p[3], int(p[4]))
                        
                    if( p[2] == '10'):
                        aux = pr.Musica( p[0], p[2], p[3], int(p[4]) )
                        

                    heappush( self.h, ( aux.getPriority(), aux ) )     

            #Si no hay proceso corriendo, pero si en cola
            if( ( self.pactual is None ) and self.h ):
                self.pactual = heappop(self.h)[1]
                self.pactual.imprimirMensaje()

            #Si hay proceso corriendo y hay en cola
            if( self.h and self.pactual ):

                pcandidato = self.h[0][1]
                
                if( self.pactual.getPriority() > pcandidato.getPriority() ):
                    heappush( self.h, (self.pactual.getPriority(), self.pactual ) )
                    self.pactual = heappop(self.h)[1]
                    self.pactual.imprimirMensaje()

                if( self.pactual.correr() ):
                    self.pactual = heappop(self.h)[1]
                    self.pactual.imprimirMensaje()
            #Si es el ultimo proceso
            elif( ( not self.h ) and self.pactual ):
                if( self.pactual.correr() ):
                    self.pactual = None

            tiempo_actual += 1





