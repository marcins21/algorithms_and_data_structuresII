from collections import defaultdict
import numpy as np

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.list_of_edges = defaultdict(list)
        self.list_of_vertecies = []
        self.counter=0
        self.result = []
        self.list_of_wages = defaultdict(list)
	
    # Add edge to a graph
    def add_edge(self, node1, node2,wage):       
        self.list_of_edges[node1].append(node2)
        self.list_of_wages[wage].append([node1,node2])

    def delete_all_edges_from_vertex(self,node1):
        #del self.list_of_edges[0]
        del self.list_of_edges[node1]
        
	# Print a graph representation
    def print_edge_list(self):
        for k,v in self.list_of_edges.items():
            print(k,v)

    def print_edge_wage(self):
        for k,v in self.list_of_wages.items():
            print(k,v)
    
    def amount_of_edges_going_out_of_vertex(self,node):
        return len(self.list_of_edges[node])
    
    def amount_of_edges_goin_in_vertex(self):
        dicionary_of_in_links = {}
        [dicionary_of_in_links.setdefault(x,0) for items in self.list_of_edges.values() for x in items]
        for k, v in self.list_of_edges.items():
            for i in v:
                dicionary_of_in_links[i] += 1
        return dicionary_of_in_links
    
    def get_all_vertecies(self):
        for k,v in self.list_of_edges.items():
            if k not in self.list_of_vertecies:
                self.list_of_vertecies.append(k)
            for link in v:
                if link not in self.list_of_vertecies:
                    self.list_of_vertecies.append(link)

        #print(self.list_of_vertecies)
        return self.list_of_vertecies
    
    def get_edge_wages(self):
        return self.list_of_wages
    
    def get_edge_list(self):
        return self.list_of_edges
    
    

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
    
    graph = Graph(amound_of_vertecies)
    #doddwanie krawedzi
    for ed in edges:
        graph.add_edge(ed[0],ed[1],ed[2])

    return graph


def main():
    g = reading_from_file("floyd-warshall/GrafTest23.txt")
    n = len(g.get_all_vertecies())

    matrix = np.full((n, n), np.inf)  # wypełnienie macierzy nieskończonościami
    np.fill_diagonal(matrix, 0) # digonale 

    # Filling matrix with wages
    wage_of_edges = g.get_edge_wages()
    for k,v in wage_of_edges.items():
        for item in v:
            matrix[item[0]][item[1]] = k

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k]+matrix[k][j]:
                    matrix[i][j] = matrix[i][k]+matrix[k][j]

    #sprawdzenie cykli
    for i in range(n):
        for j in range(n):
            if i==j and matrix[i][j] != 0:
                print("W macierzy są cykle")
                break
    

            
    print(matrix)
    #print(matrix[3][6])

    
    
main()