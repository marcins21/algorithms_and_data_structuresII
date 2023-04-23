# implementation of graph 
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self,number_of_vertecies):
        self.number_of_vertecies = number_of_vertecies
        self.list_of_edges = defaultdict(list)
        self.list_of_wages = defaultdict(list)
        self.list_of_all_vertecies = []
        self.visited = []


    def check_neighbour(self,node):
        if node not in self.get_all_vertecies():
            print(f"\nPodanego wierzchołka {node} nie ma w grafie")
            return False
        
        for k,v in self.list_of_edges.items():
            if k == node:
                return v

    def addEdge(self,node1,node2,wage=None):
        self.list_of_edges[node1].append(node2)
        self.list_of_wages[wage].append([node1,node2])

        #Tracking all vertecies
        self.list_of_all_vertecies.append(node1)
        self.list_of_all_vertecies.append(node2)

    def delete_all_edges_from_vertex(self,vertex):
        if vertex in self.list_of_edges.keys():
            del self.list_of_edges[vertex]
        else:
            print(f"\nWrong Vertex given '{vertex}' cannot be deleted because doesn't exist")

    def delete_edge(self,node1,node2):
        if node1 not in self.list_of_edges.keys():
            print(f"\nCannot delete edge vertex '{node1}' doesn't exists")
            return 0
        self.list_of_edges[node1].remove(node2)

    def get_all_vertecies(self):
        return self.list_of_all_vertecies
      
    def print_edges(self):
        for k,v in self.list_of_edges.items():
            print(k,v)

    def print_wages(self):
        for k,v in self.list_of_wages.items():
            print(k,v)

    def get_number_of_vertecies(self):
        return self.number_of_vertecies


    def DFS_util(self,v,vistied):
        vistied.add(v)
        print(v, end=" ")
        for neighbor in self.list_of_edges[v]:
            if neighbor not in vistied:
                self.DFS_util(neighbor,vistied)

    def DFS(self,v):
        visited = set()
        self.DFS_util(v,visited)


        
def reading_graph_from_file(path):
    counter = 0
    with open(path,"r") as file1:
        for line in file1:
            counter+=1
    edges = []
    with open(path,"r") as file:
        read_content = file.readlines()
        amound_of_vertecies = int(read_content[0])
        for i in range(1,counter):
            edge = read_content[i].split()
            edges.append([int(edge[0]),int(edge[1])])

    graph = Graph(amound_of_vertecies)
    for ed in edges:
        graph.addEdge(ed[0],ed[1])

    return graph
    



def main():
    g = reading_graph_from_file("kolokwium1/graf.txt")
    g.print_edges()
    
    g.DFS(1)
    
    
main()