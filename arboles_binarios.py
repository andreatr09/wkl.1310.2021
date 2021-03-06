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
			if nodo.right == None:
				nodo.right = NodoArbol( value )
			else:
				self.__insert__( nodo.right , value )

	def __recorrido__in( self , nodo ):
		if nodo != None: ## NOTE: Nodo que no sea vacio
			self.__recorrido__in( nodo.left )
			print( nodo.data , end = "," )
			self.__recorrido__in( nodo.right )

	def _recorrido_pos( self , nodo ):
		   if nodo:
			   self.__recorrido_pos(nodo.left)
			   self.__recorrido_pos(nodo.right)
			   print(nodo.data, end=", ")

	def _recorrido_pre( self , nodo ):
		   if nodo:
			   self.__recorrido_pre(nodo.left)
            	self.__recorrido_pre(nodo.right)
            	print(nodo.data, end=", ")

	def transversal( self, format = "inorden" ):
		if format == "inorden":
			self.__recorrido__in( self.__root )
		elif format == "preorden":
			print( "RECORRIDO EN PRE" )
			self.__recorrido_pre( self.__root )
		elif format == "posorden":
			print( "POSORDEN" )
			self.__recorrido_pos( self.__root )
		else:
			print( "ERROR , ESE FORMATO NO EXISTE" )

	def search( self , value ):
		if self.__root:
			return None
		else:
			return self.__search( self.__root , value )

	def __search( self , nodo , value ):
		if nodo == None ## NOTE: VACIO ??? , CASO BASE
			print("CASO BASE")
			return None
		elif nodo.data == value: # NOTE: COSO BASE DE RECURSIVIDAD
			print("ENCONTRADO")
			return nodo
		elif value < nodo.data:
			print("BUSCAR A LA IZQUIERDA")
			return self.__search( nodo.left , value )
		else:
			print("BUSCAR A LA DERECHA")
			return self.__search( nodo.right , value )

	def remove( self , value ):
		if self.__root == None:
			print( "NO HAY NADA QUE ELIMINAR" )
		else:
			self._remove( padre_hi , padre_hd , actual , value )

	def _remove( padre_hi , padre_hd , actual , value ):
		if actual == None:
			print( "CASO BASE" )
			return None
		elif actual.data == value: #CASO BASE
			print( "ENCONTRADO: " , actual.data )
			# NOTE: CASO UNO: HOJA
			if actual.left == None and actual.right == None:
				if padre_hi != None:
					padre_hi.left = None
				else:
					padre_hd.right = None
			# NOTE: CASO DOS: CON UN HIJO
			if ( actual.left != None and actual.right == None ) or ( actual.left == None and actual.right != None ):
				print( "Es un nodo con un hijo" , actual.data )
				if actual.left != None:
					actual.data = actual.left.data
					actual.left = None
				else:
					actual.data = actual.right.data
					actual.righ = None
			# NOTE: CASO TRES: CON LOS DOS HIJOS

			#return actual
		elif value < actual.data:
			print( "BUSCAR A LA IZQUIERDA" )
			self._remove( actual , None , actual.left , value )
		else:
			print( "BUSCAR A LA DERECHA" )
			self._remove( None , actual , actual.right , value )
