l# -*- coding: cp1252 -*-
import time
from multiprocessing import *
from controller import *
from historial import *
from agenda import *


if __name__ == '__main__':

    value= Queue()
    nombre = "empty"
 
    while(nombre == "empty"):
            comando = raw_input( "Desea leer un archivo(s/n)")
            if( comando == "s" ):
                nombre = raw_input( "Ingrese el nombre del archivo: ")
                try:
                    archivo = open( nombre, 'r', 0 )
                    archivo.close()
                except IOError:
                    print "El archivo ", nombre ," no existe"
                    nombre = "empty"

            elif( comando == "n" ):
                nombre = ''
            else:
                print "Comando no valido"
                nombre = "empty"

    c = Controller()
    p1 = Process( target = c.simular, args = (value, nombre) )
    p1.start()
    time.sleep(0.5)

    
    while 1:

        comando = raw_input( "Ingrese un comando: \n")

        if comando == 'lc' or comando == 'quit' or comando == 'hl' or comando == 'rl' or comando == 'em' or comando == 'rm' or comando == 'ac' or comando == 'mu' or comando == 'ru' or comando=='ju' or comando=='ms' or comando=='top' or comando=='lista':
            if comando=='lc':
                lista_contactos=[]
                
                archivo = open( "agenda.txt", 'r', 0 )
                i=0
                for line in archivo:
                    aux_agenda = line.strip().split( ';' )
                    print "("+str(i)+") "+aux_agenda[0]
                    lista_contactos.append(aux_agenda)
                    i+=1
                archivo.close()
                print "Para llamar pulse el numero entre () "
                comando=(raw_input("Ingrese comando: "))
                try:
                    comando=int(comando)
                    if comando<=len(lista_contactos):
                       dur = raw_input("Ingrese duracion: ")
                       aux = pr.Llamada( 'hacer_llamada', '1',  '0', lista_contactos[comando][1], dur )
                       value.put(aux)
                except ValueError: print ""

            if comando == 'quit':
                p1.terminate()
                break

            if comando =='hl':
                num = raw_input( "Ingrese un numero: \n")
                dur = raw_input("Ingrese duracion: \n")
                aux = pr.Llamada( 'hacer_llamada', '1',  '0', num, dur )
                value.put(aux)

            if comando == 'rl':
                num = raw_input( "Ingrese un numero: \n")
                dur = raw_input("Ingrese duracion: \n")
                aux = pr.Llamada( 'recibir_llamada', '2',  '0', num, dur )
                value.put(aux)

            if comando == 'em':
                num = raw_input("Ingrese un numero: \n")
                texto = raw_input("Ingrese el texto: \n")
                aux = pr.Mensaje( 'Enviando mensaje:', 3, 2, num, texto)
                value.put(aux)

            if comando == 'rm':
                num = raw_input("Ingrese un numero: \n")
                texto = raw_input("Ingrese el texto: \n")
                aux = pr.Mensaje( 'Recibiendo mensaje:', 3, 2, num, texto)
                value.put(aux)

            if comando == 'ac':
                num = raw_input("Ingrese el numero que desea agregar\n")
                nombre = raw_input("Ingrese el nombre del contacto\n")
                aux = pr.Contacto( "Creando nuevo contacto", 5, 6, nombre, num)
                value.put(aux) 

            if comando == 'pc':
                tiempo = raw_input("Ingrese el tiempo de ejecucion:\n")
                aux = pr.Cualquier( "Corriendo proceso indeterminado...\n", 6, 10 )
                value.put(aux)

            if comando == 'mu':
                aux = pr.Ubicacion( "Mandando ubicacion..\n", 7, 7)
                value.put(aux)

            if comando == 'ru':
                duracion = int(raw_input("Ingrese duracion del envio:\n"))
                aux = pr.Ubicacion( "Viendo ubicacion..\n", 8, 7, duracion)
                value.put(aux)

            if comando == 'ju':
                nombre = raw_input("Ingrese nombre del juego\n")
                duracion = int( raw_input("Ingrese tiempo de juego\n") )
                aux = pr.Jugar( nombre, 9, 8, duracion )
                value.put(aux)

            if comando == 'ms':
                duracion = int( raw_input("Ingrese el tiempo de duracion\n") )
                aux = pr.Musica( "Escuchando musica", 10, 8, duracion )
                value.put(aux)

            if comando=='top':
                value.put('top')

            if comando == 'lista':            
                print "\n*Comandos disponibles*\n"
                print "Para hacer una llamada: \t\t\thl"            
                print "Para recibir una llamada: \t\t\trl"
                print "Para enviar un mensaje: \t\t\tem"
                print "Para recibir un mensaje: \t\t\trm"
                print "Para desplegar la lista de contactos: \t\tlc"
                print "Para agregar un contacto: \t\t\tac"
                print "Para mandar su ubicacion: \t\t\tmu"
                print "Para recibir una ubicacion: \t\t\tru"
                print "Para jugar: \t\t\t\t\tju"
                print "Para escuchar musica: \t\t\t\tms"
                print "Para desplegar los procesos en ejecucion: \ttop"
                print "Para apagar el celular: \t\t\tquit\n"
                
        else:
            print "\nComando no valido. Para desplegar los comandos disponibles utilice el comando \"lista\"\n"
        time.sleep(1)

        






