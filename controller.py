from heapq import *
import process as pr


class Controller:
    def __init__(self):
        print "hola"


    def simular(self, h, nombre):
        tiempo_actual = 0
        
        entrantes = []

        archivo = open( "example.txt", 'r', 0 )
        for line in archivo:
            aux = line.strip().split( ';' )
            if( aux[2] == '1' or aux[2] == '2' or aux[2] == '3' or aux[2] == '4' ):
                entrantes.append( aux )

        archivo.close()


        while( True ):

            #Agrego los procesos que vienen entrando
            for p in entrantes:
                if( p[1] == str(tiempo_actual) ):
                    if( p[2] == '1' or p[2] == '2'):
                        aux = pr.Llamada( p[0], p[2], p[3], p[4], p[5] )
                        heappush( h, ( aux.getPriority(), aux ) )               #ESTO Tiene que ESTAR AFUERA DE ESTE IF!!!!!!!!

                    if( p[2] == '3' or p[2] == '4'):
                        aux = pr.Mensaje( p[0], p[2], p[3], p[4], p[5] )
                        heappush( h, ( aux.getPriority(), aux ) )

            if(h):
                aux = heappop(h)[1]

                #Corre un instante y si no termina lo devolvemos a la cola
                if( not aux.correr() ):
                    heappush( h, ( aux.getPriority(), aux ) )

            tiempo_actual += 1
