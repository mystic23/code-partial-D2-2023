from BTS import *
from node import Nodo

tree = bts()
#Inserción individual
#tree.insert(5)
#tree.insert(3)
#tree.insert(7)
#tree.insert(2)
#tree.insert(4)
#tree.insert(6)
#tree.insert(8)

#-> Insercion de varios
#values = [5,3,7,2,4,6,8]

#tree.insert_several(values)
#ARMANDO EL ARBOL MANUALMENTE
c = Nodo('A')
c.left = Nodo('B')
c.left.left = Nodo('D')
c.left.left.left = Nodo('G')
c.left.left.left.left = Nodo('K')
c.left.left.right = Nodo('H')
c.left.left.right.left = Nodo('L')
c.left.left.right.right = Nodo('M')
c.left.left.right.left = Nodo('L')
c.right = Nodo('C')
c.right.left = Nodo('E')

tree.insert(c)
tree.insert(c.left)
tree.insert(c.left.left )
tree.insert(c.left.left.left )
tree.insert(c.left.left.left.left)
tree.insert(c.left.left.right)
tree.insert(c.left.left.right.left)
tree.insert(c.left.left.right.right)
tree.insert(c.left.left.right.left)
tree.insert(c.right)
tree.insert(c.right.left)

#print(tree.search(5))  # True
#print(tree.search(10)) # False

print("Arbol antes de eliminar un nodo")
tree.InOrderPrint(tree.root)
print()

#tree.delete(6)
print("Arbol despuesde eliminar un nodo - InOrder")
tree.InOrderPrint(tree.root)
print("\nArbol despuesde eliminar un nodo - PreOrder")
tree.PreOrderPrint(tree.root)
print("\nArbol despuesde eliminar un nodo - PostOrder")
tree.PostOrderPrint(tree.root)
print()
