from colas import Queue,BoundedPriorityQueue

q1 = Queue()
q1.euqueue(3)
q1.euqueue(33)
q1.euqueue(23)
print( q1.to_string() )

print( "PRUEBA 2 DE Queue" )
c1 = { "id": 1 , "nombre": "Luna" , "balance": 20.5 }
c2 = { "id": 2 , "nombre": "Duke" , "balance": 3456.5 }
c3 = { "id": 3 , "nombre": "Buddy" , "balance": 1000000.0 }

atencion = Queue()
atencion.euqueue( c1 )
atencion.euqueue( c2 )
atencion.euqueue( c3 )
print( atencion.to_string() )
siguiente = atencion.dequeue()
print( "Bienvenido Sr. { siguiente['nombre'] } , en qué podemos servirle el día de hoy" )
print(atencion.to_string())

print("Pruebas de las colas con prioridad acotada")

maestre = { "prioridad" : 4 , "descripcion" : "Maestre" , "personas" : ["Juan P" , "Luna T"] }
niños = { "prioridad" : 2 , "descripcion" : "Niños" , "personas" : ["Santi H" , "Angel H"] }
mecanincos = { "prioridad" : 4 , "descripcion" : "Mecanicos" , "personas" : ["Diana T" , "Maria Z"] }

cpa = BoundedPriorityQueue( 7 )
cpa.enqueue( maestre['prioridad'] , maestres )
cpa.enqueue( niños['prioridad'] , niños )
cpa.enqueue( mecanicos['prioridad'] , mecanicos )
cpa.to_string()
