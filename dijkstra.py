#  ACTIVIDAD: Dijkstra - 19/11/2021

from collections import defaultdict
import heapq


class Graph:

    def __init__(self):
        self.graph = defaultdict(dict)

    def addEdge(self, u, v, d):
        self.graph[u][v] = d

    def dijkstra(self, s):
        distances = {distance: 9999999 for distance in self.graph.keys()}
        distances[s] = 0
        pq = [(0, s)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return self.display(s, distances)

    def display(self, s, distances):
        print('Distancia desde "' + s + '" hasta:')
        for vertex, distance in distances.items():
            print('  - ' + vertex + ': ' + str(distance))


# CREACION DE GRAFO
g = Graph()

g.addEdge('El Rosario', 'Instituto del Petróleo', 5)
g.addEdge('El Rosario', 'Tacuba', 3)

g.addEdge('Instituto del Petróleo', 'El Rosario', 5)
g.addEdge('Instituto del Petróleo', 'Deportivo 18 de Marzo', 1)
g.addEdge('Instituto del Petróleo', 'La Raza', 1)

g.addEdge('Deportivo 18 de Marzo', 'Instituto del Petróleo', 1)
g.addEdge('Deportivo 18 de Marzo', 'La Raza', 1)
g.addEdge('Deportivo 18 de Marzo', 'Martín Carrera', 1)

g.addEdge('Martín Carrera', 'Deportivo 18 de Marzo', 1)
g.addEdge('Martín Carrera', 'Consulado', 2)

g.addEdge('La Raza', 'Instituto del Petróleo', 1)
g.addEdge('La Raza', 'Deportivo 18 de Marzo', 1)
g.addEdge('La Raza', 'Consulado', 2)
g.addEdge('La Raza', 'Guerrero', 1)

g.addEdge('Consulado', 'Martín Carrera', 2)
g.addEdge('Consulado', 'La Raza', 2)
g.addEdge('Consulado', 'Oceanía', 2)
g.addEdge('Consulado', 'Morelos', 1)

g.addEdge('Tacuba', 'El Rosario', 3)
g.addEdge('Tacuba', 'Hidalgo', 6)
g.addEdge('Tacuba', 'Tacubaya', 4)

g.addEdge('Guerrero', 'La Raza', 1)
g.addEdge('Guerrero', 'Garibaldi', 0)
g.addEdge('Guerrero', 'Hidalgo', 0)

g.addEdge('Garibaldi', 'Guerrero', 0)
g.addEdge('Garibaldi', 'Bellas Artes', 0)
g.addEdge('Garibaldi', 'Morelos', 2)

g.addEdge('Oceanía', 'Consulado', 2)
g.addEdge('Oceanía', 'San Lázaro', 2)
g.addEdge('Oceanía', 'Pantitlán', 2)

g.addEdge('Hidalgo', 'Tacuba', 6)
g.addEdge('Hidalgo', 'Guerrero', 0)
g.addEdge('Hidalgo', 'Bellas Artes', 0)
g.addEdge('Hidalgo', 'Balderas', 1)

g.addEdge('Bellas Artes', 'Garibaldi', 0)
g.addEdge('Bellas Artes', 'Hidalgo', 0)
g.addEdge('Bellas Artes', 'Salto de Agua', 1)
g.addEdge('Bellas Artes', 'Pino Suárez', 2)

g.addEdge('Morelos', 'Consulado', 1)
g.addEdge('Morelos', 'Garibaldi', 2)
g.addEdge('Morelos', 'San Lázaro', 0)
g.addEdge('Morelos', 'Candelaria', 0)

g.addEdge('San Lázaro', 'Morelos', 0)
g.addEdge('San Lázaro', 'Oceanía', 2)
g.addEdge('San Lázaro', 'Candelaria', 0)
g.addEdge('San Lázaro', 'Pantitlán', 5)

g.addEdge('Balderas', 'Hidalgo', 1)
g.addEdge('Balderas', 'Centro Médico', 2)
g.addEdge('Balderas', 'Tacubaya', 5)
g.addEdge('Balderas', 'Salto de Agua', 0)

g.addEdge('Salto de Agua', 'Bellas Artes', 1)
g.addEdge('Salto de Agua', 'Balderas', 0)
g.addEdge('Salto de Agua', 'Pino Suárez', 1)
g.addEdge('Salto de Agua', 'Chabacano', 2)

g.addEdge('Pino Suárez', 'Bellas Artes', 2)
g.addEdge('Pino Suárez', 'Salto de Agua', 1)
g.addEdge('Pino Suárez', 'Candelaria', 0)
g.addEdge('Pino Suárez', 'Chabacano', 1)

g.addEdge('Candelaria', 'Morelos', 0)
g.addEdge('Candelaria', 'San Lázaro', 0)
g.addEdge('Candelaria', 'Pino Suárez', 0)
g.addEdge('Candelaria', 'Jamaica', 1)

g.addEdge('Tacubaya', 'Tacuba', 4)
g.addEdge('Tacubaya', 'Balderas', 5)
g.addEdge('Tacubaya', 'Centro Médico', 2)
g.addEdge('Tacubaya', 'Mixcoac', 2)

g.addEdge('Centro Médico', 'Balderas', 2)
g.addEdge('Centro Médico', 'Tacubaya', 2)
g.addEdge('Centro Médico', 'Chabacano', 1)
g.addEdge('Centro Médico', 'Zapata', 3)

g.addEdge('Chabacano', 'Pino Suárez', 1)
g.addEdge('Chabacano', 'Centro Médico', 1)
g.addEdge('Chabacano', 'Jamaica', 0)
g.addEdge('Chabacano', 'Salto de Agua', 2)
g.addEdge('Chabacano', 'Santa Anita', 1)
g.addEdge('Chabacano', 'Ermita', 5)

g.addEdge('Jamaica', 'Candelaria', 1)
g.addEdge('Jamaica', 'Chabacano', 0)
g.addEdge('Jamaica', 'Pantitlán', 4)
g.addEdge('Jamaica', 'Santa Anita', 0)

g.addEdge('Pantitlán', 'Oceanía', 2)
g.addEdge('Pantitlán', 'San Lázaro', 5)
g.addEdge('Pantitlán', 'Jamaica', 4)

g.addEdge('Santa Anita', 'Chabacano', 1)
g.addEdge('Santa Anita', 'Jamaica', 0)
g.addEdge('Santa Anita', 'Atlalilco', 5)

g.addEdge('Mixcoac', 'Tacubaya', 2)
g.addEdge('Mixcoac', 'Zapata', 2)

g.addEdge('Zapata', 'Centro Médico', 3)
g.addEdge('Zapata', 'Mixcoac', 2)
g.addEdge('Zapata', 'Ermita', 2)

g.addEdge('Ermita', 'Chabacano', 5)
g.addEdge('Ermita', 'Zapata', 2)
g.addEdge('Ermita', 'Atlalilco', 1)

g.addEdge('Atlalilco', 'Santa Anita', 5)
g.addEdge('Atlalilco', 'Ermita', 1)


# ALGORITMO DE DIJKSTRA
print("----------------------------------------------------")
print("Algoritmo de Dijkstra")
print("----------------------------------------------------")
g.dijkstra('El Rosario')


# DISCLAIMER. Código basado en las versiones disponibles en:
# bfs.py
# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
