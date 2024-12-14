import graphviz
import collections

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}   #lista sąsiedztwa z wagami
        self.visited = False #metoda do określania czy node został odwiedzony przy metodzie topology sort

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        nbrs = []
        for nbr in self.connectedTo:
            nbrs.append(nbr.id)
        return nbrs

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setDistance(self, d):
        self.dist = d

    def getDistance(self):
        return self.dist

    def setPred(self, p):
        self.pred = p

    def getPred(self):
        return self.pred

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def get_vertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def add_edge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.add_vertex(f)
        if t not in self.vertList:
            nv = self.add_vertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    #lista sąsiadów(dzieci)
    def get_neighbors(self,n):
        if n in self.vertList:
            return self.vertList[n].getConnections()
        else:
            return None

    #pokazanie wszystkich połączeń w grafie
    def get_edges(self):
        edges = []
        for vertex in self.vertList:
            neighbor = self.get_neighbors(vertex)
            for nbr in neighbor:
                edges.append((vertex, nbr))
        return edges

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    #reprezentacja grafu w jezyku dot(jak odczytac vertexy i edge)
    def visualize(self):
        dot = graphviz.Digraph()
        for vert in self.get_vertices():
            dot.node(str(vert))
        for edge in self.get_edges():
            dot.edge(str(edge[0]), str(edge[1]))
        return dot

    #przeszukiwanie wszerz
    def bfs(self, root):
        queue = collections.deque([root])
        visited = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
            for item in self.get_neighbors(node):
                if item not in visited:
                    queue.append(item)
        return visited

    #znalezienie najkrótszej drogi
    def shortest_path(self, node1, node2):
        visited = []

        #kolejka na drogi
        queue = [[node1]]

        #jeśli to ten sam node
        if node1 == node2:
            node = [node1]
            return f"Shortest path from {node1} to {node2} : {node}, with distance: {len(node)-1}"

        # dopóki nie jest pusta kolejka- nie wyczerpiemy możliwych dróg
        while queue:
            path = queue.pop(0)
            node = path[-1]

            #jeśli node nie jest w visited, żeby nie nawarstwiały nam się takie same drogi w kolejce
            if node not in visited:
                neighbours = self.get_neighbors(node)

                #patrzymy na dzieci noda i dodajemy ścieżki to kolejki
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    #jeśli osiągnięty neighbour to ten którego szukamy to to jest droga szukana
                    if neighbour == node2:
                        return f"Shortest path from {node1} to {node2} : {new_path}, with distance: {len(new_path)-1}"
                visited.append(node)
        #jeśli pętla się skończyła to znaczy że nie ma drogi łączącej danych nodów
        return f"There is no path connecting {node1} and {node2}"

    #iteracja po wszystkich nodach do których chcemy otrzymać drogę
    def paths(self,node):
        for vert in self.get_vertices():
            print(self.shortest_path(node,vert))


    #przeszukiwanie w głąb
    def dfs(self,node, visited=[]):
        if node not in visited:
            visited.append(node)
            for neighbour in self.get_neighbors(node):
                self.dfs(neighbour,visited)
        return visited

    #topologiczne sortowanie(chodzenie po nodach i ich dzieciach, a później wracanie się do początku -rekurencja)
    def topology(self,start=0,output_stack = [],visited=[]):
        if not self.vertList[start].visited:
            self.vertList[start].visited = True
            for nbr in self.get_neighbors(start):
                self.topology(nbr,output_stack)
            output_stack.insert(0, start)
            visited.append(start)

        return output_stack

    #funkcja do wejścia w rekurencje
    def topology_sort(self):
        visited = []
        stack = []

        for vert in self.get_vertices():
            if vert not in visited:
                self.topology(vert,stack)
        return stack

if __name__=="__main__":
    #graf3, topologiczny sort powinien nie zadziałać (bo pętla)
    g = Graph()
    g.add_edge("a", "b")
    g.add_edge("b", "d")
    g.add_edge("a", "d")
    g.add_edge("d", "e")
    g.add_edge("e", "b")
    g.add_edge("b", "c")
    g.add_edge("e", "f")
    g.add_edge("f", "c")
    print(g.get_edges())
    print("BFS",g.bfs("a"))
    print("DFS",g.dfs("a"))
    print("TOPOLOGY", g.topology_sort())
    print("---")
    print(g.visualize())
    g.paths("a")
    #graf2
    g1 = Graph()
    g1.add_edge("a", "b")
    g1.add_edge("c", "b")
    g1.add_edge("a", "d")
    g1.add_edge("b", "d")
    g1.add_edge("d", "e")
    g1.add_edge("d", "h")
    g1.add_edge("e", "f")
    g1.add_edge("f", "h")
    print(g1.get_edges())
    print("BFS", g1.bfs("a"))
    print("DFS", g1.dfs("a"))
    print("TOPOLOGY", g1.topology_sort())
    print("---")
    print(g1.visualize())
    g1.paths("a")
    #graf1
    g2 = Graph()
    g2.add_edge("a", "b")
    g2.add_edge("a", "c")
    g2.add_edge("b", "c")
    g2.add_edge("c", "d")
    g2.add_edge("b", "f")
    g2.add_edge("g", "b")
    g2.add_edge("g", "f")
    g2.add_edge("f", "d")
    g2.add_edge("f", "e")
    print(g2.get_edges())
    print("BFS", g2.bfs("a"))
    print("DFS", g2.dfs("a"))
    print("TOPOLOGY", g2.topology_sort())
    print("---")
    print(g2.visualize())
    g2.paths("a")
