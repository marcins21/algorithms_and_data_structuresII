from collections import defaultdict
import numpy as np
import heapq
import math
class Graph:
    # Constructor
    def __init__(self, directed=True):
    
        self.directed = directed
        self.list_of_edges = defaultdict(list)
        self.list_of_vertecies = []
        self.counter=0
        self.result = []
        self.list_of_wages = defaultdict(list)
        self.vertex = set()
	
    # Add edge to a graph
    def add_edge(self, node1, node2,wage):       
        self.list_of_edges[node1].append(node2)
        self.list_of_wages[wage].append([node1,node2])
        self.vertex.add(node1)
        self.vertex.add(node2)
        

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
    
    def get_all_vertex(self):
        return len(self.vertex)
    
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
    result = []
    try:
        with open(path,'r') as file:
            for line in file:
                result.append(line)
        return result
    except Exception:
        print(f"\nNie znaleziono pliku {path} podaj poprawna sciezke\nFile not Found {path} give correct path ")

def parsing_data(data:list):
    amount_of_substancies = int(data[0])
    substancies = defaultdict(list)
    amount_of_processes = int(data[amount_of_substancies+1])
    proccesses = []
    for i in range(1,amount_of_substancies+1):
        substancies[i].append(int(data[i].replace("\n","")))
    
    for j in range(amount_of_processes,len(data)):
        proccesses.append([data[j]])
    cleaned_processes = [[item.strip() for item in sublist] for sublist in proccesses]
    
    return amount_of_substancies, amount_of_processes, cleaned_processes, substancies

def find_all_paths(graph,m):
    # utworzenie pustej listy na wszystkie ścieżki
    paths = []
    def dfs_paths(start, end, path=[]):
        # dodanie bieżącego wierzchołka do ścieżki
        path = path + [start]
        
        # warunek zakończenia: jeśli bieżący wierzchołek jest wierzchołkiem końcowym
        if start == end:
            path.insert(0,start)
        
            #Ilosc operacji M
            if len(path) < m:
                paths.append(path)
        
        # rekurencyjnie znajdujemy wszystkie możliwe ścieżki od sąsiadujących wierzchołków
        for neighbor in graph[start]:
            if neighbor not in path:
                dfs_paths(neighbor, end, path)
    
    # wywołujemy funkcję dfs_paths dla każdego sąsiada wierzchołka 1
    for neighbor in graph[1]:
        dfs_paths(neighbor, 1)
    
    # zwracamy wszystkie znalezione ścieżki
    return paths


def main():
    print("\nPodaj nazwe pliku *.txt z ktorego mam czytac dane  (umiesc ten plik w tym samym folderze co ten skrypt) \nChcesz uzyc domyslnej nazwy 'input.txt'? Kliknij [ENTER] \n")
    user_input = input("Nazwa: ")
    if user_input == '':
        user_input = "input.txt"
    try:
     n,m,proccesses,substancies = parsing_data(reading_from_file(user_input))
    except Exception:
        print(f"\nCos poszlo nie tak, popatrz na informacje powyzej\nSomething went wrong check info above\n")
        return 
    
    parsed_processes = []
    # Printing
    print("\n----INFO----\n")
    print(f"Ilosc Substancji -> '{n}' ")
    print(f"Ilosc Dopuszczalnych Procesow -> '{m}' ")
    print(f"\nSubstancje oraz ich cena index: 1-zloto")
    for k,v in substancies.items():
        print(k,v)

    #Parsing To int all data
    print(f"\n--PROCESY-- indexy: 0-1 substancje 2-cena za przetworzenie substancji 0->1")
    for element in proccesses:
        parsed_processes.append(element[0].split())
    proccesses = [[int(item) for item in sublist] for sublist in parsed_processes]
    
    for process in proccesses:
        print(process)
    
    #Computing
    # m - max number of processes avaliable
    g = Graph()
    # dodaj krawędzie
    for edge in proccesses:
        g.add_edge(edge[0], edge[1], edge[2])
    

    matrix_n = n+1
    matrix = np.full((matrix_n, matrix_n), np.inf)  # wypełnienie macierzy nieskończonościami
    np.fill_diagonal(matrix, 0) # digonale 

    # Filling matrix with wages
    
    for proccess in proccesses:
        matrix[proccess[0]][proccess[1]] = proccess[2]
        
    #print(matrix)
    
    for k in range(matrix_n):
        for i in range(matrix_n):
            for j in range(matrix_n):
                if matrix[i][j] > matrix[i][k]+matrix[k][j]:
                    matrix[i][j] = matrix[i][k]+matrix[k][j]

    dijkstra_graph = {}
    for i in range(1,matrix_n):
        dijkstra_graph[i] = {}
        for j in range(len(matrix)):
            if matrix[i][j] != np.inf and i != j:
                dijkstra_graph[i][j] = matrix[i][j]
                    
    

    print(f"\nFloydWarshal Graph - Contrustion of new graph using dijkstra algorithm")
    for k,v in dijkstra_graph.items():
        print(k,v) #DEBUG INFO
        #pass
    
    paths = find_all_paths(dijkstra_graph,m)
    print(f"\nWszystkie dostepne sciezki dojscia od elemenu numer 1-złoto do elemnetu 1-złoto \n{paths}")
    
    price_of_all = []
    result = []
    for i in range(len(paths)):
        res = 0
        price = []
        for j in range(len(paths[i])-1):
            if paths[i][j] != 1:
                price.append(substancies[paths[i][j]][0])      
            res += dijkstra_graph[paths[i][j]][paths[i][j+1]]
        result.append(res)
        price_of_all.append(price)
        
    just_gold = 0.5*int(substancies[1][0])
    #Debug Info
    #print(price_of_all)
    #print(result)
    for k in range(len(price_of_all)):
        result[k] += (0.5*max(price_of_all[k]))


    print(f"\nWartosci podstawione do konkrtenych sciezek podanych powyzej z uwzglednionym cłem (+0.5*cena najdrozszego materialu) \n{result}")
            
    wynik = min(result)
    if wynik < just_gold:
        print(f"\nWYNIK {wynik} \n")
    else:
        print(f"\nWYNIK {just_gold} \n")
    #Debug Info
    #print(dijkstra_graph)

main()
