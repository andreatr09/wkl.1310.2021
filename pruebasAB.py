from arboles_binarios import BinarySerchTree

abb = BinarySerchTree()
abb.insert(50)
abb.insert(30)
abb,insert(40)
abb.insert(35)
abb.insert(89)
abb.insert(89)


abb.transversal()

abb.transversal("preorden")
abb.transversal("posorden")

res = abb.search(25)
print("EL RESULTADO ES: {res}")

abb.remove(35)
abb.transversal()
