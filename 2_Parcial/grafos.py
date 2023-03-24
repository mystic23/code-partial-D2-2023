class Directed_Graph:
    
    def __init__(self) -> None:
        self.graph_dict = {}
    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict = []
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        
        
class Edge:
    def __init__(self, v1, v2) -> None:
        self.v1 = v1
        self.v2 = v2
    
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def __str__(self) -> str:
        return self.v1.get_name() + ' --->' + self.v2.get_name()

class Vertex:
    
    def __init__(self, name) -> None:
           self.name = name
    
    def get_name(self):
        return self.name
    def __str__(self) -> str:
        return self.name