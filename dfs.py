#  ACTIVIDAD: Depth First Search - 19/10/2021

from pyvis import network as net
from IPython.core.display import display, HTML


class Grafo:

    matriz = []
    aristas = []

    def __init__(self, v, e):
        self.v = v
        self.e = e
        Grafo.matriz = [[0 for i in range(v)]
                        for j in range(v)]

    def agregarArista(self, inicio, e):
        Grafo.matriz[inicio][e] = 1
        Grafo.matriz[e][inicio] = 1
        Grafo.aristas.append([inicio, e])

    def DFS(self, inicio, visitado):
        print(inicio, end=' ')
        visitado[inicio] = True
        for i in range(self.v):
            if(Grafo.matriz[inicio][i] == 1 and (not visitado[i])):
                self.DFS(i, visitado)

    def grafico(self):
        g = net.Network(height='400px', width='50%', heading='Grafo')
        i = 0
        while i < self.v:
            g.add_node(i)
            i = i + 1
        for par in self.aristas:
            g.add_edge(par[0], par[1])
        g.show('grafo.html')
        display(HTML('grafo.html'))


# CREACION DEL GRAFO
# Definir número de vértices y aristas.
v, e = 8, 9

# Inicializar el grafo.
G = Grafo(v, e)

# Definir aristas existentes.
G.agregarArista(0, 1)
G.agregarArista(0, 3)
G.agregarArista(1, 4)
G.agregarArista(3, 4)
G.agregarArista(2, 3)
G.agregarArista(2, 5)
G.agregarArista(4, 5)
G.agregarArista(5, 6)
G.agregarArista(6, 7)

# DEPTH FIRST SEARCH
visitado = [False] * v
G.DFS(0, visitado)

# REPRESENTACION VISUAL DEL GRAFO
# Diponible en archivo "grafo.html"
G.grafico()


# DISCLAIMER. Código parcialmente basado en la versión disponible en:
# https://www.geeksforgeeks.org/implementation-of-dfs-using-adjacency-matrix/
