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
    
    def dfs(self, vertice, visitados):
        visitados.add(vertice)
        for arista in self.aristas:
            if vertice in arista[:2]:
                vecino = arista[0] if arista[1] == vertice else arista[1]
                if vecino not in visitados:
                    self.dfs(vecino, visitados)

    def es_conexo(self):
        visitados = set()
        self.dfs(list(self.vertices)[0], visitados)
        return len(visitados) == len(self.vertices)

print("\n")
print("Forma de esclavos D: )")
print("---------------------")
grafo = Grafo()
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')

grafo.agregar_arista('A', 'B', 4)
grafo.agregar_arista('A', 'C', 4)
grafo.agregar_arista('B', 'C', 2)
grafo.agregar_arista('C', 'D', 3)
grafo.agregar_arista('C', 'E', 2)
grafo.agregar_arista('C', 'F', 4)
grafo.agregar_arista('D', 'F', 3)
grafo.agregar_arista('E', 'F', 3)

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



print("------------Parte punto 3---------")
print("la función dfs recibe un vértice y un conjunto de visitados y "+ "\n" +
      "realiza una búsqueda en profundidad a partir del vértice dado," + "\n" +
      "marcando todos los vértices alcanzables como visitados. La función" + "\n" +
      "es_conexo utiliza el método dfs para verificar si se puede alcanzar" + "\n" +
      "todos los vértices del grafo partiendo del primer vértice en la lista de vértices. ")
if grafo.es_conexo():
    print("El grafo es conexo")
else:
    print("El grafo no es conexo")

