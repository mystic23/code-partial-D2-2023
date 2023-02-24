from node import Nodo

class BTS:

##Raiz  
    def __init__(self) :
     
        self.root = None 
## Insert individual, manual , list

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
        else :
            if current.right is None:
                current.right = new
            else: 
                self.insert_recursive(new, current.right)
        current.height = 1 + max(self.get_hight(current.left), self.get_hight(current.right))## Buscar 
   
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
        
## Eliminar
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

##Encontrar al hijo   
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
## altura
    def get_hight(self, current: Nodo) -> int:
       
        if not current:
            return 0
        return current.height
    
    def height_tree(self):
        if self.root is None:
            return 0
        else: return self.root.height
    
#La familia gg
    def search_dad(self, value):
        return self.search_dad_recursive(self.root, value, None)
    
    def search_dad_recursive(self, current, value, dad):
        if current is None:
            return None
        elif value is current.value:
            return dad
        elif value < current.value:
            return self.search_dad_recursive(current.left, value, current)
        else: 
            return self.search_dad_recursive(current.right, value, current)
        
    def search_grandpa(self, value):
        dad =self.search_dad(value)
        if dad is None:
            return None
        else: 
            return self.search_dad(dad.value)
    
    def search_uncle(self, value): 
        dad = self.search_dad(value)
        if dad is None:
            return None
        else:
            grandpa = self.search_grandpa(value)
            if grandpa is None:
                return None
            elif dad is grandpa.left:
                return grandpa.right if grandpa.right is not None else None
            else: 
                return grandpa.left if grandpa.left is not None else None
        
    def min(self):
       if self.root is None:
           return None
       else: return self.min_recursive(self.root)
       
    def min_recursive(self, current):
        if current.left is None:
            return current.value
        else: return self.min_recursive(current.left)
    
    def max(self):
        if self.root is None:
           return None
        else:
           return self.max_recursive(self.root)
    
    def max_recursive(self, current):
        if current.right is None:
            return current.value
        else: return self.max_recursive(current.right)
        
    def get_nodes_by_level(self):
        if self.root is None:
            return {}

        nodes_by_level = {}
        current_level = 1
        nodes_queue = [self.root]

        while nodes_queue:
            current_level_nodes = []
            nodes_in_queue = len(nodes_queue)

            for i in range(nodes_in_queue):
                current_node = nodes_queue.pop(0)
                current_level_nodes.append(current_node.value)

                if current_node.left:
                    nodes_queue.append(current_node.left)
                if current_node.right:
                    nodes_queue.append(current_node.right)

            nodes_by_level[current_level] = current_level_nodes
            current_level += 1

        for level, nodes in nodes_by_level.items():
            print(f"Level {level}: {nodes}")

        return nodes_by_level
    def get_node_level(self, value):
        current = self.root
        level = 1
        while current is not None:
            if current.value == value:
                return level
            elif value < current.value:
                current = current.left
            else:
                current = current.right
            level += 1
        return None
