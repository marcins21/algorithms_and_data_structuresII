# implementation of graph 
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self,number_of_vertecies):
        self.number_of_vertecies = number_of_vertecies
        self.list_of_edges = defaultdict(list)
        self.list_of_wages = defaultdict(list)
        self.list_of_all_vertecies = set()
        self.visited = []

    def check_neighbour(self,node):
        if node not in self.get_all_vertecies():
            print(f"\nPodanego wierzchołka {node} nie ma w grafie")
            return False
        
        for k,v in self.list_of_edges.items():
            if k == node:
                return v

    def addEdge(self,node1,node2,wage=None):
        self.list_of_edges[node1].append({node2:wage})
        self.list_of_wages[wage].append([node1,node2])

        #Tracking all vertecies
        self.list_of_all_vertecies.add(node1)
        self.list_of_all_vertecies.add(node2)

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
    
    def amount_of_edges_goin_in_vertex(self):
        counter = 0
        dicionary_of_in_links = {}
        queue =  []

        for item in self.list_of_all_vertecies:
            dicionary_of_in_links.setdefault(item,0)
            queue.append(item)
        
        #XD! Brute-forcing algorithm XD!
        for i in range(len(queue)):
            checking = queue[i]
            for k,v in self.list_of_edges.items():
                for key in v:
                    for keys in key:
                        if keys == checking:
                            dicionary_of_in_links[checking] += 1
            counter +=1
        return dicionary_of_in_links
    

    def topological_sort(self,links):
        queue = []
        result = []
        
        for k,v in links.items():
            #print(k,v)
            if v == 0:
                queue.append(k)
       
        while queue:
            a = queue.pop(0)
            result.append(a)

            for neighbour in self.list_of_edges[a]:
                for k in neighbour.keys():
                    if links[k] != 0:
                        links[k] -= 1

                for j in neighbour.keys():
                    if links[j] == 0: 
                        queue.append(j)
        print(result)
                  

    def BFS(self,starting):
        queue = []
        queue.append(starting)
        self.visited.append(starting)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for neigbour in self.list_of_edges[s]:
                for k in neigbour.keys():
                    if k not in self.visited:
                        queue.append(k)
                        self.visited.append(k)

    def DFS_util(self,visited,starting):
        visited.add(starting)
        print(starting,end=" ")
        for neighbour in self.list_of_edges[starting]:
            for k in neighbour.keys():
                if k not in visited:
                    visited.add(k)
                    self.DFS_util(visited,k)

    def DFS(self,starting):
        vistied  = set()
        self.DFS_util(vistied,starting)
              

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
            #int(edge[2])
            edges.append([int(edge[0]),int(edge[1])])

    graph = Graph(amound_of_vertecies)
    for ed in edges:
        #ed[2]
        graph.addEdge(ed[0],ed[1])

    return graph
    

def main():
    g = reading_graph_from_file("kolokwium1/graf.txt")
    #g.print_edges()

    print("BFS")
    g.BFS(1)
    print("\nDFS")
    g.DFS(1)

    print()
    #links = g.amount_of_edges_goin_in_vertex()
    #g.topological_sort(links)
    #g.print_edges()
    
main()