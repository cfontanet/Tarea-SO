class agenda:

    def __init__(self):
        self.contactos = []
        archivo = open( "agenda.txt", 'r', 0 )

        for line in archivo:
            aux = line.strip().split( ';' )
            self.contactos.append( aux )
            
        archivo.close()

    # Muestra todos los registros de la agenda
    def mostrar(self):
        for c in self.contactos:
            print c[0] + ' ' + c[1]


    # retorna el nombre del contacto en la posicion entregada
    def getName ( self, posicion ):
        return self.contactos[posicion][0]


    # retorna el numero de la posicion entregada de la agenda
    def getNumber( self, posicion ):
        return self.contactos[posicion][1]


    # agrega un nuevo contacto a la agenda
    def agregarContacto ( self, nombre, numero):
        self.contactos.append( [ nombre, numero ])
        
        archivo = open( "agenda.txt", 'a', 0 )
        archivo.write( nombre + ';' + numero + '\n')
        archivo.close()


# a = agenda()

# a.mostrar()

# a.agregarContacto( 'Nicolas Mora' , '91234567')

# a.mostrar()

