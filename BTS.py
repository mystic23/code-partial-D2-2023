from node import Nodo

class BTS:
    
    def __init__(self) :
        self.root = None 
      
    def insert(self, value):
        new = Nodo(value)
        if self.root is None:
            self.root = new
        else:
            self.insert_recursive(new, self.root)
    
    def insert_several(self, list_value: list ):
        for value in list_value:
            self.insert(value)
    
    def insert_recursive(self, new, current):
        if new.value < current.value:
            if current.left is None:
                current.left = new
            else:
                self.insert_recursive(new,current.left)
        elif new.value > current.value:
            if current.right is None:
                current.right = new
            else: 
                self.insert_recursive(new, current.right)
    
    def search(self, value):
        return self.search_recursive(value, self.root)
    
    def search_recursive(self, value, current):
        if current is None:
            return f" No esta en el arbol :("
        elif value == current.value:
            return f" Esta en el arbol :)"
        elif value < current.value:
            return self.search_recursive(value, current.left)
        else:
            return self.search_recursive(value,current.right)
        
    def delete(self, value):
        self.root = self.delete_recursive(value, self.root)
    
    def delete_recursive(self, value, current):
        if current is None:
            return None
        elif value < current.value:
            current.left = self.delete_recursive(value, current.left)
            return current
        elif value > current.value:
            current.right = self.delete_recursive(value,current.right)
            return current
        else:
            
            if current.left is None and current.right is None:
                return None    #no tiene hijos
            #nodo con un hijo
            if current.left is None:
                return current.right
            if current.right is None:
                return current.right
            #nodo dos hijos
            son = self.find_son(current.right)
            current.value = son.value
            current.right = self.delete_recursive(son.value, current.right)
            return current
        
    def find_son(self, current):
        while current.left is not None:    
            current =  current.left 
            return current 
    
 ##RECORRIDOS
    def InOrderPrint(self, current):
        if current is None:
            return
        else:
            self.InOrderPrint(current.left)
            print(current , end=' ')
            self.InOrderPrint(current.right)
            
    def PreOrderPrint(self, current):
        if current is None:
            return
        else:
            print(current, end=' ')
            self.PreOrderPrint(current.left)
            self.PreOrderPrint(current.right)

    def PostOrderPrint(self, current):
        if current is None:
            return
        else:
            self.PostOrderPrint(current.left)
            self.PostOrderPrint(current.right)
            print(current, end=' ')  
        
## %%  
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


print(tree.search(5))  # True
print(tree.search(10)) # False

print("Arbol antes de eliminar un nodo")
tree.InOrderPrint(tree.root)
print()

#tree.delete(6)
print("Arbol despuesde eliminar un nodo - InOrder\n")
tree.InOrderPrint(tree.root)
print("\nArbol despuesde eliminar un nodo - PreOrder")
tree.PreOrderPrint(tree.root)
print("\nArbol despuesde eliminar un nodo - PostOrder")
tree.PostOrderPrint(tree.root)
print()

