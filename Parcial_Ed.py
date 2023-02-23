from node import Nodo
from BinaryTree import BTS
###Solución Tercer punto 
print("Solución tercer punto")
#Creacion manual del arbol
tree = BTS()
tree.root = Nodo('A')
tree.root.left = Nodo('B')
tree.root.left.left = Nodo('D')
tree.root.left.left.left = Nodo('G')
tree.root.left.left.left.left = Nodo('K')
tree.root.left.left.right = Nodo('H')
tree.root.left.left.right.left = Nodo('L')
tree.root.left.left.right.right = Nodo('M')
tree.root.left.left.right.left = Nodo('L')
tree.root.right = Nodo('C')
tree.root.right.left = Nodo('E')

print("Arbol   - InOrder")
tree.InOrderPrint(tree.root)
print("\nArbol - PreOrder")
tree.PreOrderPrint(tree.root)
print("\nArbol - PostOrder")
tree.PostOrderPrint(tree.root)
print()
##Solucion
#Arbol   - InOrder
# K  G  D  L  H  M  B  A  E  C
#Arbol - PreOrder
# A  B  D  G  K  H  L  M  C  E
#Arbol - PostOrder
# K  G  L  M  H  D  B  E  C  A


###Solución segundo punto
print("Solución segundo punto")
##Preguntas:
##Realizar un algoritmo que dado un BST, escriba el padre del nodo cuya
#información es la menor y mayor del árbol, también debe decir en qué nivel se
#encontraron los padres. (Queda a su disposición que información quiere mostrar
#del nodo padre).

