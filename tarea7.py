class NodoDoble:
	def __init__( self, value, siguiente = None , anterior = None ):
		self.data = value
		self.next = siguiente
		self.prev = anterior

# NOTE: Constructor
class DoubleLinkedList:
	def __init__( self ):
		self.__head = NodoDoble( None , None , None )
		self.__tail = NodoDoble( None , None , None )
		self.__head.next = self.__tail
		self.__tail.prev = self.__head
		self.__size = 0
		print( f" head : {self.__head} " )
		print( f" tail : {self.__tail} " )

	# NOTE: Saber la cantidad de elementos en la lista
	def get_size( self ):
		apuntador = self.__head
		cuenta = 0
		#Argumentar la cuenta +1 cada vez que haya nuevo Nodo
		while apuntador is not None:
			cuenta = cuenta + 1
			apuntador = apuntador.siguiente
		return cuenta

	# NOTE: Preguntar si esta vacia
	def is_empty (self):
        if self.__head is None:
			return True
		else:
			return False

	# NOTE: Agregar elementos a la lista
	def append( self , value ):
		#lista vacia
		if self.__head is None:
			nuevoNodo = Nodo(dato)
			self.__head = nuevoNodo
			return
		#Crear un apuntador a la cabeza sino esta vacia
		apuntador = self.__head
		#El nodo se convierta a None
		while apuntador.siguiente is not None:
			apuntador = apuntador.siguiente
		#crear nuevo nodo
		nuevoNodo = Nodo(dato)
		#Insertar el nodo al final de la fila
		apuntador.siguiente = nuevoNodo
		#conectar el nodo con el ultimo que exista
		nuevoNodo.anterior = apuntador

	# NOTE: Buscar a partir de tail regresar la posicion
	def find_from_tail( self , value ):


	# NOTE: Buscar a partir de head regresar la posicion
	def find_from_head( self , value ):


	# NOTE: Eliminar a partir de tail
	def remove_from_tail( self , value ):
		if self.__tail.siguiente is None:
			self.__tail = None
			return
		apuntador = self.__tail
		while apuntador.siguiente is not None:
			apuntador = apuntador.siguiente
			apuntador.anterior.siguiente = None
			#Elimina el ultimo elemento

	# NOTE: Eliminar a partir de head
	def remove_from_head( self , value ):
		if self.__head.siguiente is None:
			self.__head = None
		self.__head = self.__head.siguiente
		self.__head.anterior = None
		#Elimina el primer elemento

	# NOTE: Recorrido desde head
	def transversal( self ):
	 	apuntador= self.__head
		while apuntador != None:
			print( f" { apuntador.data } ->", end="" )
			apuntador = apuntador.anterior.siguiente

	# NOTE: Recorrido desde el final
	def reverse_transversal( self ):
