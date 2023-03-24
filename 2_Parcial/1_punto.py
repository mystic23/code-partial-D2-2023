import heapq  # importamos la biblioteca heapq para utilizar una cola de prioridad


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_vertice(self, v):
        """
        Agrega un nuevo vértice al grafo.
        
        Args:
            v (str): el nombre del nuevo vértice que se va a agregar.
        """
        self.vertices[v] = []

    def agregar_arista(self, u, v, peso):
        """
        Agrega una nueva arista al grafo.
        
        Args:
            u (str): el nombre del vértice origen de la arista.
            v (str): el nombre del vértice destino de la arista.
            peso (float): el peso o costo de la arista.
        """
        if u not in self.vertices:
            self.agregar_vertice(u)
        if v not in self.vertices:
            self.agregar_vertice(v)
        self.aristas[(u, v)] = peso
        self.vertices[u].append(v)

    def eliminar_vertice(self, v):
        """
        Elimina un vértice y todas sus aristas del grafo.
        
        Args:
            v (str): el nombre del vértice que se va a eliminar.
        """
        if v in self.vertices:
            # Eliminar aristas que conectan al vértice
            for u, vecinos in self.vertices.items():
                if v in vecinos:
                    self.aristas.pop((u, v), None)
                    self.vertices[u] = [vecino for vecino in vecinos if vecino != v]
            
            # Eliminar el vértice
            self.vertices.pop(v, None)
    def camino_minimo(self, inicio, fin):
        """
        Encuentra el camino mínimo y la distancia mínima desde un vértice de inicio hasta un vértice de fin,
        utilizando el algoritmo de Dijkstra.

        Args:
            inicio (str): El vértice de inicio del camino.
            fin (str): El vértice de fin del camino.

        Returns:
            tuple: Una tupla con dos elementos:
                - Una lista de vértices que representan el camino mínimo desde inicio hasta fin.
                - La distancia mínima desde inicio hasta fin.
                  Si no hay camino posible, retorna None para ambos elementos.
        """
        if inicio not in self.vertices or fin not in self.vertices:
            return None, None

        # Aplicar Dijkstra para encontrar las distancias mínimas a cada nodo
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0
        heap = [(0, inicio)]
        visitados = set()
        padre = {}

        while heap:
            (dist, actual) = heapq.heappop(heap)
            if actual in visitados:
                continue
            visitados.add(actual)

            for vecino in self.vertices[actual]:
                peso = self.aristas[(actual, vecino)]
                distancia_alternativa = dist + peso
                if distancia_alternativa < distancias[vecino]:
                    distancias[vecino] = distancia_alternativa
                    padre[vecino] = actual
                    heapq.heappush(heap, (distancia_alternativa, vecino))

        # Construir camino mínimo
        if distancias[fin] == float('inf'):
            return None, None

        camino = [fin]
        while camino[-1] != inicio:
            camino.append(padre[camino[-1]])
        camino.reverse()

        return camino, distancias[fin]


# Ejemplo de uso
grafo = Grafo()

# Agregar vértices
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')

# Agregar aristas con costos
#primero las externas
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 2)
grafo.agregar_arista('C', 'E', 3)
grafo.agregar_arista('B', 'D', 2)
grafo.agregar_arista('D', 'F', 7)
grafo.agregar_arista('E', 'F', 1)

##Segundo las internas
grafo.agregar_arista('B', 'C', 1)
grafo.agregar_arista('B', 'E', 3)
grafo.agregar_arista('D', 'E', 2)
grafo.agregar_arista('D', 'C', 4)


print("Esto muestra el grafo ")
for u, vecinos in grafo.vertices.items():
    for v in vecinos:
        camino, peso = grafo.camino_minimo('A', u)
        print(u, "->", v)


print("Esto es A")
for destino in ['A', 'B', 'C', 'D', 'E', 'F']:
    camino, peso = grafo.camino_minimo('A', destino)
    print(f"Camino mínimo desde A a {destino}: {peso}")
    print(camino)
print(f"-----------------------------")

print("Esto es B")
for destino in ['A', 'B', 'C', 'D', 'E', 'F']:
    camino, peso = grafo.camino_minimo('B', destino)
    print(f"Camino mínimo desde B a {destino}: {peso}")
    print(camino)
    
print(f"-----------------------------")    
print("Esto es C")
for destino in ['A', 'B', 'C', 'D', 'E', 'F']:
    camino, peso = grafo.camino_minimo('C', destino)
    print(f"Camino mínimo desde C a {destino}: {peso}")
    print(camino)

print(f"-----------------------------")
print("Esto es D")
for destino in ['A', 'B', 'C', 'D', 'E', 'F']:
    camino, peso = grafo.camino_minimo('D', destino)
    print(f"Camino mínimo desde D a {destino}: {peso}")
    print(camino)

print(f"-----------------------------")
print("Esto es E")
for destino in ['A', 'B', 'C', 'D', 'E', 'F']:
    camino, peso = grafo.camino_minimo('E', destino)
    print(f"Camino mínimo desde E a {destino}: {peso}")
    print(camino)

print(f"-----------------------------")
print("Esto es F")
for destino in ['A', 'B', 'C', 'D', 'E', 'F']:
    camino, peso = grafo.camino_minimo('F', destino)
    print(f"Camino mínimo desde F a {destino}: {peso}")
    print(camino)

    
