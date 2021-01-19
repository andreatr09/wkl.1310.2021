class NodoArbol:
	def __init__( self , value, left=None , right=None ):
		self.data = value
		self.left = left
		self.right = right


class BinarySerchTree:
	def __init__( self ):
		self.__root = None

	def insert( self , value ):
		#REGLA 1:
		if self.__root == None: ## NOTE: Es equivalente a : self.__root is None
			self.__root = NodoArbol( value , None , None )
		#REGLA 2:
		else:
			self.__insert__( self.__root , value )

	def __insert__( self , nodo , value ):
		if modo.data == value:
			print( "EL DATO YA EXISTE , NO SE INGRESA NADA" )
		elif value < nodo.data:
			#REGLA 1: NODO DE LA IZQUIERDA
			if nodo.left == None:
				nodo.left = NodoArbol( value )
			#REGLA 2:
			else:
				self.__insert__( nodo.left , value )
		else:
			if nodo.right == Nonne:
				nodo.right = NodoArbol( value )
			else:
				self.__insert__( nodo.right , value )

	def __recorrido__in( self , nodo ):
		if nodo != None: ## NOTE: Nodo que no sea vacio
			self.__recorrido__in( nodo.left )
			print( nodo.data , end = "," )
			self.__recorrido__in( nodo.right )

	def transversal( self , format="inorden" ):
		if format == "inorden":
			self.__recorrido__in( self.__root )
		elif format == "preorden":
			print( "RECORRIDO EN PRE" )
		elif format == "posorden":
			print( "POSORDEN" )
		else:
			print( "ERROR , ESE FORMATO NO EXISTE" )
