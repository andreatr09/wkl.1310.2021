def factorial( n ):
	if n == 0:
		return 1
	else:
		return factorial( n-1 ) * n

def printRev( n ):	# NOTE: Recibe el numero tres y lo imprime en la pantalla
	if n > 0:	# NOTE: Imprime una secuencia en reversa hasta llegar a un numero mayor a cero
		print( n )
		printRev( n - 1 )

def fibonacci( n ):
	if n == 1 or n == 0:
		return n
	else:
		return( fibonacci( n - 1 ) + fibonacci( n - 2 ) )

def main():
	for num in range( 1,10,1 )
	r = factorial( num )
	print( f"El factorial de { num } es { r }" )

def main2():
	printRev( 3 )

main2()
