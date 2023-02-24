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

tree1 = BTS()
values1 = [6, 5, 4, 5, 6, 2, 9,8,7,10]
tree1.insert_several(values1)
print("---------------")
print("ALTURA DEL ARBOL: ", tree1.height_tree())

print("--Minimos--")
min = tree1.min()
print("altura minimo del arbol:", tree1.get_hight(Nodo(min)))

print("altura del valor menor del arbol ", tree1.get_hight(Nodo(min)))

print("Papá del minimo", tree1.search_dad(min), )
print("abuelo del minimo",  tree1.search_grandpa(min))
print("tio del minimo",  tree1.search_uncle(min))

print ("-- Maximos --")
print("Valor maximo del arbol ", tree1.max())
max = tree1.max()

print("altura del valor maximo del arbol ", tree1.get_hight(Nodo(max)))

dad = tree1.search_dad(max)

print("Papá del maximo",tree1.search_dad(max), "alltura: ", tree1.get_hight(dad) )

grandpa = tree1.search_grandpa(max) 
print("abuelo del maximo", tree1.search_grandpa(max) , "altura : ", tree1.get_hight(grandpa) )

uncle = tree1.search_uncle(max)
print("tio del maximo", uncle ,"altura : ", tree1.get_hight(uncle))

tree1.get_nodes_by_level()