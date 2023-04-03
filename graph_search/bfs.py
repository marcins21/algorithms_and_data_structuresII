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

    def bfs_search(self,s):
        visited = [False] * (self.m_num_of_nodes+1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.edges[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
            
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

    print(f"\nbfs dla 1 ")
    g.bfs_search(1)
    print(f"\nbfs dla 2 ")
    g.bfs_search(2)
    print(f"\nbfs dla 4 ")
    g.bfs_search(4)
    print(f"\nbfs dla 7 ")
    g.bfs_search(7)
    print(f"\nbfs dla 11")
    g.bfs_search(11)
 
main()