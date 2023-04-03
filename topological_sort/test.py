from collections import defaultdict
 
# Class to represent a graph
 
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack)  # return list in reverse order
        return stack
 
 
# Driver Code
if __name__ == '__main__':


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
        g.addEdge(ed[0],ed[1])


 
    # Function Call
    result = g.topologicalSort()


    if len(result) < amound_of_lines:
        print("graf Posiada cykle")
    else:
        print("Graf jest acykliczny")
# This code is contributed by Neelam Yadav