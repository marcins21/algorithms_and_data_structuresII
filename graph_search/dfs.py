from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.edges = defaultdict(list)
	
    def addEdge(self, node1, node2):        
        self.edges[node1].append(node2)
        
    def print_edge_list(self):
        for k,v in self.edges.items():
            print("edge ", k, ": ", v)

    def check_neighboors(self,vertex):
        if self.edges[vertex]:
            return True
        else:
            return False

    def get_neighboors(self,vertex):
        neighboors = []
        for edge in self.edges[vertex]:
            neighboors.append(edge)
        return neighboors
    
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.edges[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

           
def main():
    #Wczytanie pliku grapf.txt
    edges = []

    #W vscode trzeba podmienic "graph_search\graf.txt"
    with open("graf.txt","r") as file:
        read_content = file.readlines()
        amound_of_lines = int(read_content[0])
        for i in range(1,amound_of_lines):
            edge = read_content[i].split()
            edges.append([int(edge[0]),int(edge[1])])
    
    g = Graph(amound_of_lines)

    #doddwanie krawedzi
    for ed in edges:
        g.addEdge(ed[0],ed[1])

    print(f"\nAlgorytm DFS dla 1 ")    
    g.DFS(1)
    print(f"\nAlgorytm DFS dla 2 ")   
    g.DFS(2)
    print(f"\nAlgorytm DFS dla 4 ")   
    g.DFS(4)
    print(f"\nAlgorytm DFS dla 7 ")   
    g.DFS(7)
    print(f"\nAlgorytm DFS dla 11 ")   
    g.DFS(11)

 
main()