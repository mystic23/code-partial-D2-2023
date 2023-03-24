from node import Nodo
from BinaryTree import BTS

tree = BTS()
#Inserción individual
#tree.insert(5)
#tree.insert(3)
#tree.insert(7)
#tree.insert(2)
#tree.insert(4)
#tree.insert(6)
#tree.insert(8)

#-> Insercion de varios
values = [5,3,7,2,4,6,8]
tree.insert_several(values)

#height_tree = tree.Obheight()
#height_node = tree.Obheight_(tree.root.right)

#print(f'La altura del arbol es { height_tree}')
#print(f'la altura del nodo 7 es {height_node}')
#ARMANDO EL ARBOL MANUALMENTE
#tree.root = Nodo('A')
#tree.root.left = Nodo('B')
#tree.root.left.left = Nodo('D')
#tree.root.left.left.left = Nodo('G')
#tree.root.left.left.left.left = Nodo('K')
#tree.root.left.left.right = Nodo('H')
#tree.root.left.left.right.left = Nodo('L')
#tree.root.left.left.right.right = Nodo('M')
#tree.root.left.left.right.left = Nodo('L')
#tree.root.right = Nodo('C')
#tree.root.right.left = Nodo('E')



#print(tree.search(5))  # True
#print(tree.search(10)) # False

#print("Arbol antes de eliminar un nodo")
#tree.InOrderPrint(tree.root)
#print()

#tree.delete(6)
print("Arbol  - InOrder")
tree.InOrderPrint(tree.root)
print("\nArbol  - PreOrder")
tree.PreOrderPrint(tree.root)
print("\nArbol  - PostOrder")
tree.PostOrderPrint(tree.root)
print()
