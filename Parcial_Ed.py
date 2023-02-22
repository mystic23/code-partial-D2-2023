from BTS import BTS
###Solución Tercer punto 
#InOrder traversal
#A B C D E G H K L M 
# PreOrder traversal
#A B D C G E K H L M
# PostOrder traversal
#C E H M L K G D B A


tree = BTS()
values = [5,3,7,2,4,6,8]

tree.insert_several(values)


print(tree.search(5))  # True
print(tree.search(10)) # False

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
