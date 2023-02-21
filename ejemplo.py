class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data): 
        if self.data is None:
            self.data = data
        else: 
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                    
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else: 
                    self.right.insert(data)

def InOrderPrint(r):
    
    if r is None:
        return
    else:
        InOrderPrint(r.left)
        print(r.data, end=' ')
        InOrderPrint(r.right)
        
def PreOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        PreOrderPrint(r.left)
        PreOrderPrint(r.right)

def PostOrderPrint(r):
    if r is None:
        return
    else:
        PostOrderPrint(r.left)
        PostOrderPrint(r.right)
        print(r.data, end=' ')

def makeList(r):
    if r is None:
        return 
    else:
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)
        makeList(r.right)
    return d        
if __name__ == "__main__":
    root = Node("g")
    root.insert("c")
    root.insert("b")
    root.insert("a")
    root.insert("e")
    root.insert("d")
    root.insert("f")
    root.insert("i")
    root.insert("h")
    root.insert("j")
    root.insert("k")


#1. Print all nodes InOrder
print(" InOrder traversal")
InOrderPrint(root)

#2. Print all nodes PreOrder
print("\n PreOrder traversal")
PreOrderPrint(root)

#3. Print all nodes PostOrder
print("\n PostOrder traversal")
PostOrderPrint(root)

print("\n")
#4. Adjency List 
print("Adjency List \n")
d = {}
aList = makeList(root)

for element in aList:
    print(f"{element}:{d[element]}")