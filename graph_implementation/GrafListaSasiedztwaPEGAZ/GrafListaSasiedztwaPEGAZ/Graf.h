#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <cstdio>
#include "edge.h"


class Graf
{
    std::vector<std::vector<edge>> vertexList;


public:
    Graf();  
    void addEdge(int i_Vertex_Index_1, int i_Vertex_Index_2);    
    bool removeEdge(int i_Vertex_Index_1, int i_Vertex_Index_2);
    bool checkEdge(int i_Vertex_Index_1, int i_Vertex_Index_2);
    int vertexDegree(int idx); 
    std::vector<int> getNeighbourIndices(int idx);
    void printNeighbourIndices(int idx);
    int getNumberOfEdges();
    void readFromFile(std::string path); 
    void print_vector();
};

