from multiprocessing import *
from process import *
from historial import *
from agenda import *

if __name__ == '__main__':

    h = []

    comando = raw_input( "Desea leer un archivo(s/n)")

    if( comando == "s" ):
        nombre = raw_input( "Ingrese el nombre del archivo: ")

    elif( comando == "n" ):
        nombre = ''

    c = Controller()
    p1 = Process( target = c.simular, args = (h, nombre) )
    p1.start()

    while 1:
        comando = raw_input( "Ingrese un comando: ")

        if comando == 'quit':
            p1.terminate()
            break





    