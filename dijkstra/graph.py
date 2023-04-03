from collections import defaultdict
from queue import PriorityQueue
import heapq as heap


array = defaultdict(list)

class Graph:
    # Constructor
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.edges = [[-1 for i in range(num_of_nodes)] for j in range(num_of_nodes)]
        self.visited = []
        
    def addEdge(self, node1, node2,weight):        
        self.edges[node1][node2] = weight
        
    def print_edge_list(self):
        for item in self.edges:
            print("edge ",item)

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


def dijkstra(G, startingNode):
	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode))
 
	while pq:
		# go greedily by always extending the shorter cost nodes first
		_, node = heap.heappop(pq)
		visited.add(node)
 
		for adjNode, weight in G[node].items():
			if adjNode in visited:	continue
				
			newCost = nodeCosts[node] + weight
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heap.heappush(pq, (newCost, adjNode))
        
	return parentsMap, nodeCosts
# def dijkstra(graph, start_vertex):
#     D = {v:float('inf') for v in range(graph.m_num_of_nodes)}
#     D[start_vertex] = 0

#     pq = PriorityQueue()
#     pq.put((0, start_vertex))

#     while not pq.empty():
#         (dist, current_vertex) = pq.get()
#         graph.visited.append(current_vertex)

#         for neighbor in range(graph.m_num_of_nodes):
#             if graph.edges[current_vertex][neighbor] != -1:
#                 distance = graph.edges[current_vertex][neighbor]
#                 if neighbor not in graph.visited:
#                     old_cost = D[neighbor]
#                     new_cost = D[current_vertex] + distance
#                     if new_cost < old_cost:
#                         pq.put((new_cost, neighbor))
#                         D[neighbor] = new_cost
#     return D



def main():
    #Wczytanie pliku grapf.txt
    edges = []

    #"dijkstra/Przykłady-20230327/Graf1.txt"
    #W vscode trzeba podmienic "graph_search\graf.txt"
    with open("dijkstra/Przykłady-20230327/Graf1.txt","r") as file:
        read_content = file.readlines()
        amound_of_lines = int(read_content[0])
        for i in range(1,amound_of_lines):
            edge = read_content[i].split()
            edges.append([int(edge[0]),int(edge[1]),int(edge[2])])
    
    g = Graph(amound_of_lines)
    #doddwanie krawedzi
    for ed in edges:
        g.addEdge(ed[0],ed[1],ed[2])

    g.print_edge_list()
    
    L,D = dijkstra(g,1)
    for vertex in range(len(D)):
        print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
main()