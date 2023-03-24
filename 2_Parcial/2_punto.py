# Importamos la biblioteca de grafos NetworkX y la biblioteca de algoritmos para encontrar árboles de expansión mínima
import networkx as nx
from networkx.algorithms import tree

print("Forma viva de hacerlo :)")
print("------------------------")
# Creamos el grafo no dirigido
G = nx.Graph()

# Agregamos los nodos al grafo
G.add_nodes_from(['6', '1', '2', '3', '4', '5', '7'])

# Agregamos las aristas al grafo junto con su costo
G.add_edge('6', '1', weight=10)
G.add_edge('1', '2', weight=28)
G.add_edge('2', '3', weight=16)
G.add_edge('3', '4', weight=12)
G.add_edge('4', '5', weight=22)
G.add_edge('5', '7', weight=24)
G.add_edge('4', '7', weight=18)
G.add_edge('7', '2', weight=14)

# Usamos el algoritmo de Kruskal para encontrar el árbol de expansión mínima
T = tree.minimum_spanning_tree(G)

# Imprimimos las aristas del árbol de expansión mínima junto con sus costos
print("Aristas del árbol de expansión mínima:")
for edge in T.edges(data=True):
    print(edge[0], '---', edge[1], 'peso:', edge[2]['weight'])

# Imprimimos el costo total del árbol de expansión mínima
total_cost = sum([edge[2]['weight'] for edge in T.edges(data=True)])
print("Costo total del árbol de expansión mínima:", total_cost)

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = []

    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)

    def agregar_arista(self, inicio, fin, costo):
        self.aristas.append((inicio, fin, costo))

    def buscar_padre(self, padres, vertice):
        if padres[vertice] == vertice:
            return vertice
        return self.buscar_padre(padres, padres[vertice])

    def unir(self, padres, rango, vertice1, vertice2):
        padre1 = self.buscar_padre(padres, vertice1)
        padre2 = self.buscar_padre(padres, vertice2)

        if rango[padre1] > rango[padre2]:
            padres[padre2] = padre1
        elif rango[padre1] < rango[padre2]:
            padres[padre1] = padre2
        else:
            padres[padre2] = padre1
            rango[padre1] += 1

    def kruskal(self):
        # Ordenamos las aristas por costo
        self.aristas.sort(key=lambda x: x[2])
        aristas_arbol = []
        padres = {}
        rango = {}

        # Inicializamos los padres y rangos para cada vértice
        for vertice in self.vertices:
            padres[vertice] = vertice
            rango[vertice] = 0

        # Aplicamos el algoritmo de Kruskal
        for arista in self.aristas:
            inicio, fin, costo = arista
            if self.buscar_padre(padres, inicio) != self.buscar_padre(padres, fin):
                self.unir(padres, rango, inicio, fin)
                aristas_arbol.append(arista)

        # Creamos un nuevo grafo con las aristas del árbol de expansión mínima
        grafo_arbol = Grafo()
        for vertice in self.vertices:
            grafo_arbol.agregar_vertice(vertice)
        for arista in aristas_arbol:
            inicio, fin, costo = arista
            grafo_arbol.agregar_arista(inicio, fin, costo)

        return grafo_arbol

print("\n")
print("Forma de esclavos D: )")
print("---------------------")
grafo = Grafo()
grafo.agregar_vertice('6')
grafo.agregar_vertice('1')
grafo.agregar_vertice('2')
grafo.agregar_vertice('3')
grafo.agregar_vertice('4')
grafo.agregar_vertice('5')
grafo.agregar_vertice('7')

grafo.agregar_arista('6', '1', 10)
grafo.agregar_arista('1', '2', 28)
grafo.agregar_arista('2', '3', 16)
grafo.agregar_arista('3', '4', 12)
grafo.agregar_arista('4', '5', 22)
grafo.agregar_arista('5', '7', 24)
grafo.agregar_arista('4', '7', 18)
grafo.agregar_arista('7', '2', 14)

arbol_expansion = grafo.kruskal()

for inicio, fin, costo in arbol_expansion.aristas:
    print(inicio, "---", fin, "peso:", costo)
    
    
costos = []
for arista in arbol_expansion.aristas:
    # Extraer el tercer valor de la tupla (el costo de la arista)
    costo = arista[2]
    # Agregar el costo a la lista de costos
    costos.append(costo)
# Sumar todos los costos para obtener el costo total
costo_total = sum(costos)
print("Costo total del árbol de expansión mínima:", costo_total)

