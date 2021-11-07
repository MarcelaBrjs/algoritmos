from collections import defaultdict
from queue import Queue


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertexNames = {}

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addVertexName(self, vertex, name):
        self.vertexNames[vertex] = name

    def BFS(self, s):
        queue = Queue()
        distances = {distance: 9999999 for distance in self.graph.keys()}
        visitedVertices = set()
        queue.put(s)
        while not queue.empty():
            vertex = queue.get()
            if vertex == s:
                distances[vertex] = 0
                visitedVertices.update({s})
            for u in self.graph[vertex]:
                if u not in visitedVertices:
                    if distances[u] > distances[vertex] + 1:
                        distances[u] = distances[vertex] + 1
                    queue.put(u)
                    visitedVertices.update({u})
        return self.display(s, distances)

    def display(self, s, distances):
        print('Distancia desde ' + self.vertexNames[s] + ' hasta:')
        for vertex, distance in distances.items():
            print('  - ' + self.vertexNames[vertex] + ': ' + str(distance))


# CREACION DE GRAFO
g = Graph()
g.addVertexName(0, 'El Rosario')
g.addVertexName(1, 'Instituto del Petróleo')
g.addVertexName(2, 'Deportivo 18 de Marzo')
g.addVertexName(3, 'Martín Carrera')
g.addVertexName(4, 'La Raza')
g.addVertexName(5, 'Consulado')
g.addVertexName(6, 'Tacuba')
g.addVertexName(7, 'Guerrero')
g.addVertexName(8, 'Garibaldi')
g.addVertexName(9, 'Oceanía')
g.addVertexName(10, 'Hidalgo')
g.addVertexName(11, 'Bellas Artes')
g.addVertexName(12, 'Morelos')
g.addVertexName(13, 'San Lázaro')
g.addVertexName(14, 'Balderas')
g.addVertexName(15, 'Salto de Agua')
g.addVertexName(16, 'Pino Suárez')
g.addVertexName(17, 'Candelaria')
g.addVertexName(18, 'Tacubaya')
g.addVertexName(19, 'Centro Médico')
g.addVertexName(20, 'Chabacano')
g.addVertexName(21, 'Jamaica')
g.addVertexName(22, 'Pantitlán')
g.addVertexName(23, 'Santa Anita')
g.addVertexName(24, 'Mixcoac')
g.addVertexName(25, 'Zapata')
g.addVertexName(26, 'Ermita')
g.addVertexName(27, 'Atlalilco')

g.addEdge(0, 1)
g.addEdge(0, 6)

g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(1, 4)

g.addEdge(2, 1)
g.addEdge(2, 4)
g.addEdge(2, 3)

g.addEdge(3, 2)
g.addEdge(3, 5)

g.addEdge(4, 1)
g.addEdge(4, 2)
g.addEdge(4, 5)
g.addEdge(4, 7)

g.addEdge(5, 3)
g.addEdge(5, 4)
g.addEdge(5, 9)
g.addEdge(5, 12)

g.addEdge(6, 0)
g.addEdge(6, 10)
g.addEdge(6, 18)

g.addEdge(7, 4)
g.addEdge(7, 8)
g.addEdge(7, 10)

g.addEdge(8, 7)
g.addEdge(8, 11)
g.addEdge(8, 12)

g.addEdge(9, 5)
g.addEdge(9, 13)
g.addEdge(9, 22)

g.addEdge(10, 6)
g.addEdge(10, 7)
g.addEdge(10, 11)
g.addEdge(10, 14)

g.addEdge(11, 8)
g.addEdge(11, 10)
g.addEdge(11, 15)
g.addEdge(11, 16)

g.addEdge(12, 5)
g.addEdge(12, 8)
g.addEdge(12, 13)
g.addEdge(12, 17)

g.addEdge(13, 12)
g.addEdge(13, 9)
g.addEdge(13, 17)
g.addEdge(13, 22)

g.addEdge(14, 10)
g.addEdge(14, 19)
g.addEdge(14, 18)
g.addEdge(14, 15)

g.addEdge(15, 11)
g.addEdge(15, 14)
g.addEdge(15, 16)
g.addEdge(15, 20)

g.addEdge(16, 11)
g.addEdge(16, 15)
g.addEdge(16, 17)
g.addEdge(16, 20)

g.addEdge(17, 12)
g.addEdge(17, 13)
g.addEdge(17, 16)
g.addEdge(17, 21)

g.addEdge(18, 6)
g.addEdge(18, 14)
g.addEdge(18, 19)
g.addEdge(18, 24)

g.addEdge(19, 14)
g.addEdge(19, 18)
g.addEdge(19, 20)
g.addEdge(19, 25)

g.addEdge(20, 16)
g.addEdge(20, 19)
g.addEdge(20, 21)
g.addEdge(20, 15)
g.addEdge(20, 23)
g.addEdge(20, 26)

g.addEdge(21, 17)
g.addEdge(21, 20)
g.addEdge(21, 22)
g.addEdge(21, 23)

g.addEdge(22, 9)
g.addEdge(22, 13)
g.addEdge(22, 21)

g.addEdge(23, 20)
g.addEdge(23, 21)
g.addEdge(23, 27)

g.addEdge(24, 18)
g.addEdge(24, 25)

g.addEdge(25, 19)
g.addEdge(25, 24)
g.addEdge(25, 26)

g.addEdge(26, 20)
g.addEdge(26, 25)
g.addEdge(26, 27)

g.addEdge(27, 23)
g.addEdge(27, 26)

# EJECUCION BREADTH FIRST TRAVERSAL
print("----------------------------------------------------")
print("Breadth First Traversal")
print("----------------------------------------------------")
g.BFS(0)


# DISCLAIMER. Código basado en la versiones disponibles en:
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# https://www.askpython.com/python/examples/distance-between-nodes-unweighted-graph
