from queue import Queue
from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.list_of_edges = defaultdict(list)
        self.list_of_vertecies = []
        self.counter=0
        self.result = []
	
    # Add edge to a graph
    def add_edge(self, node1, node2):        
        self.list_of_edges[node1].append(node2)

    def delete_edge(self,node1):
        
        #del self.list_of_edges[0]
        del self.list_of_edges[node1]
        
	# Print a graph representation
    def print_edge_list(self):
        for k,v in self.list_of_edges.items():
            print(k,v)
    
    def amount_of_edges_going_out_of_vertex(self,node):
        return len(self.list_of_edges[node])
    

    def amount_of_edges_goin_in_vertex(self):
        dicionary_of_in_links = {}
        [dicionary_of_in_links.setdefault(x,0) for items in self.list_of_edges.values() for x in items]

        for k, v in self.list_of_edges.items():
            for i in v:
                dicionary_of_in_links[i] += 1
        #print(dicionary_of_in_links)
        return dicionary_of_in_links
    

    def get_vertecies(self):
        for k,v in self.list_of_edges.items():
            if k not in self.list_of_vertecies:
                self.list_of_vertecies.append(k)
            for link in v:
                if link not in self.list_of_vertecies:
                    self.list_of_vertecies.append(link)

        #print(self.list_of_vertecies)
        return self.list_of_vertecies

    
    def topological_sort(self):
        vertecies = self.get_vertecies()
        q = Queue()
        to_delete = []
        for item in vertecies:
            if item not in self.amount_of_edges_goin_in_vertex().keys():
                to_delete.append(item)


        for i in range(self.counter,len(to_delete)):
                
                self.counter += 1
                q.put(to_delete[i])
                self.delete_edge(to_delete[i])
                self.result.append(to_delete[i])
        
        to_delete.clear()


        print(self.result)



 



def main():
    # graph = Graph(5)

    # graph.add_edge(0, 4)
    # graph.add_edge(0, 1)
    # graph.add_edge(0, 2)
    # graph.add_edge(1, 3)
    # graph.add_edge(1, 4)
    # graph.add_edge(4, 2)
    # graph.add_edge(4, 3)

    edges = []
    with open("topological_sort/Graf1.txt","r") as file:
        read_content = file.readlines()
        amound_of_lines = int(read_content[0])
        for i in range(1,97):
            edge = read_content[i].split()
            edges.append([int(edge[0]),int(edge[1]),int(edge[2])])
    
    g = Graph(amound_of_lines)
    #doddwanie krawedzi
    for ed in edges:
        g.add_edge(ed[0],ed[1])


    g.print_edge_list()
    g.topological_sort()
    g.topological_sort()

    # graph.print_edge_list()
    # print(graph.amount_of_edges_going_out_of_vertex(1))
    # print(graph.amount_of_edges_goin_in_vertex())
    # graph.get_vertecies()
    # graph.topological_sort()

    # print("Po usunieciu")
    # graph.print_edge_list()

    # print("stopnie")
    # print(graph.amount_of_edges_goin_in_vertex())

    # graph.topological_sort()


    
main()