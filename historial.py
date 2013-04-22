class historial:

    def __init__ (self):

        # Cargo los mensajes de memoria
        self.mensajes = []
        archivo = open( "mensajes.txt", 'r', 0 )

        for line in archivo:
            aux = line.strip().split( ';' )
            self.mensajes.append( aux )
            
        archivo.close()

        # Cargo las llamadas de memoria
        self.llamadas = []
        archivo = open( "llamadas.txt", 'r', 0 )

        for line in archivo:
          aux = line.strip().split( ';' )
          self.llamadas.append( aux )

        archivo.close()

    # Muestra los registros de mensajes
    def mostrar_mensajes( self ):
        for m in self.mensajes:
            print m[0] + ' ' + m[1] + ' ' + m[2]

    # Registra un mensaje nuevo
    def agregar_mensaje( self, a, numero, texto):
        # Agrego el mensaje a la lista
        self.mensajes.append( [ a, numero, texto ] )

        # Escribo el mensaje en memoria
        archivo = open( "mensajes.txt", 'a', 0 )
        archivo.write( a + ';' + numero + ';' + texto + '\n')
        archivo.close()

    # Muestra los registos de llamadas
    def mostrar_llamadas( self ):
      for m in self.llamadas:
          print m[0] + ' ' + m[1]

    # Registra una llamada nueva
    def agregar_llamada( self, a, numero):
        # Agrego la llamada a la lista
        self.llamadas.append( [ a, numero ] )

        # Escribo la llamada en memoria
        archivo = open( "llamadas.txt", 'a', 0 )
        archivo.write( a + ';' + numero + '\n')
        archivo.close()

# h = historial()
# # h.mostrar_mensajes()
# # h.agregar_mensaje( 'de', '1234', 'chao' )
# # h.mostrar_mensajes()
# h.mostrar_llamadas()
# h.agregar_llamada( 'para', '123456')
# h.mostrar_llamadas()



