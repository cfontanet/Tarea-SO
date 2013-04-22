# #! /usr/bin/env python

archivo = open( "example.txt", 'r', 0 )

stack = []

for line in archivo:

    aux = line.strip().split( ';' )
    if ( ( aux[0] == 'hacer_llamada' ) or ( aux[0] == 'recibir_llamada' ) ):
        stack.append( [ aux[0], aux[4], aux [5] ])

archivo.close()

print stack

while ( len(stack) > 0):
    print stack.pop()


def input ():

    while 1:
        a = raw_input( "Ingrese un comando: ")
        print a 
        if a == 'quit':
            break


input()