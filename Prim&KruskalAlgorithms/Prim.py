import numpy as np
from collections import defaultdict
import heapq


class WeightedUndirectedGraph:
    def __init__(self, node_count: int, edge_count: int):
        self.graph = defaultdict(list)
        self.edge_count = edge_count
        self.node_count = node_count
    

    def add_egde(self,node1,node2,weight):
        for e in range(self.edge_count):
            x, y, w = int(node1),int(node2),int(weight)
            self.graph[x].append((y, w))
            self.graph[y].append((x, w))

    def print_edges(self):
        for k,v in self.graph.items():
            print("Krawedz",k,set(v))


    def prim(self,start):
        visited = [False] * self.node_count
        min_heap = []
        total_weight = 0
        start_node = start
        path = []

        heapq.heappush(min_heap, (0, start_node))

        while min_heap:
            weight, node = heapq.heappop(min_heap)

            if visited[node]:
                continue

            if node not in path:
                path.append(node)
        

            visited[node] = True
            total_weight += weight

            for neighbor, neighbor_weight in self.graph[node]:
                if not visited[neighbor]:
                    
                    heapq.heappush(min_heap, (neighbor_weight, neighbor))

        return total_weight,path


def reading_from_file(path):

    counter = 0
    with open(path,"r") as file1:
        for line in file1:
            counter+=1
     
    edges = []
    #"topological_sort/Graf1.txt"
    with open(path,"r") as file:
        read_content = file.readlines()
        amound_of_vertecies = int(read_content[0])
        for i in range(1,counter):
            edge = read_content[i].split()
            edges.append([int(edge[0]),int(edge[1]),int(edge[2])])
    

    g = WeightedUndirectedGraph(amound_of_vertecies,len(edges))

    #doddwanie krawedzi
    for ed in edges:
        g.add_egde(ed[0],ed[1],ed[2])

    return g


#graph = reading_from_file("Prim&KruskalAlgorithms/Graf_Drzewo_MST_Algorytm_PrimaGr6.txt")
graph = reading_from_file("Prim&KruskalAlgorithms/test.txt")
print(graph)


graph.print_edges()
print("\n\n")
w,v = graph.prim(4)
print(f"Suma wag '{w}' Kolejnosc wierzcholkow: '{v}' ")

w,v = graph.prim(11)
print(f"Suma wag '{w}' Kolejnosc wierzcholkow: '{v}' ")
