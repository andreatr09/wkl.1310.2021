class Nodo:
    def __init__( self, value, siguiente= None ):
        self.data = value #encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__( self ):
        self.__head = None

        def is_empty (self):
            return self.__head == None
