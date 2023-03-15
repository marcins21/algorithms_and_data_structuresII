#include "Graf.h"
#include "edge.h"

edge::edge(int i_Vertex_Index1, int i_Vertex_Index2)
{
    vertex_Index1 = i_Vertex_Index1;
    vertex_Index2 = i_Vertex_Index2;
    waga = 0;
}

edge::edge(int i_Vertex_Index_1, int i_Vertex_Index_2, float i_weight)
{
    vertex_Index1 = i_Vertex_Index_1;
    vertex_Index2 = i_Vertex_Index_2;
    waga = i_weight;
}

int counter=0;
Graf::Graf(){
    counter++;
    std::cout<<"\nGraph "<<counter<<" Created\n";
}

// ?
void Graf::createVertices(int amount){
    std::cout<<"\n?"<<std::endl;
}

// Done 
void Graf::addEdge(int vertex_ind1, int vertex_ind2){
    std::vector<edge> edge_vec;
    edge* vertex_edge= new edge(vertex_ind1,vertex_ind2);
    edge_vec.push_back(*vertex_edge);
    Graf::vertexList.push_back(edge_vec);
}

// Done 
bool Graf::removeEdge(int vertex_ind1, int vertex_ind2){

    if(Graf::checkEdge(vertex_ind1,vertex_ind2) == 1){
        for(auto it = Graf::vertexList.begin(); it != Graf::vertexList.end(); it++){

        if(it.base()->data()->vertex_Index1 == vertex_ind1 && it.base()->data()->vertex_Index2 == vertex_ind2){
            Graf::vertexList.erase(it);
            std::cout<<"\nUsuwam Krawedz: "<<vertex_ind1<<" "<<vertex_ind2<<" \n";
            return true;

        }else{
            ++it;
        }
        }
    }
    return false;
}   

// Done
int Graf::vertexDegree(int idx){
    int count = 0;
    for(auto it = Graf::vertexList.begin(); it != Graf::vertexList.end(); it++){
        if(it.base()->data()->vertex_Index1 == idx && it.base()->data()->vertex_Index2){
            count++;
        }
    }
    return count;
}

//Done
std::vector<int> Graf::getNeighbourIndices(int idx){

    std::vector<int> indices;
    for(auto it = Graf::vertexList.begin(); it != Graf::vertexList.end(); it++){
        if(it.base()->data()->vertex_Index1 == idx && it.base()->data()->vertex_Index2){
            indices.push_back(it.base()->data()->vertex_Index2);
        }
    }
    return indices;
}

//Done 
void Graf::printNeighbourIndices(int idx){
    std::cout<<"\nNeighbour Indices of "<<idx<<": ";
    for(auto i: Graf::getNeighbourIndices(idx)){
        std::cout<<i<<" ";
    }
}

//Done 
int Graf::getNumberOfEdges(){
    int sumUp=0;
    for(auto it = Graf::vertexList.begin(); it != Graf::vertexList.end(); it++){
        if(it.base()->data()->vertex_Index1){
            sumUp++;
        }
    }
    return sumUp;
}

// Done
bool Graf::checkEdge(int vertex_ind1, int vertex_ind2){
    for(auto i : Graf::vertexList){
        if( i.data()->vertex_Index1 == vertex_ind1 && i.data()->vertex_Index2 ==vertex_ind2){
            //Debug Info
            //std::cout<<i.data()->vertex_Index1<<" "<<i.data()->vertex_Index2<<std::endl;
            return true;
        }
    }
    return false;
}

// Done 
void Graf::print_vector(){
    std::cout<<"\nGraph:"<<std::endl;
     for(auto i : Graf::vertexList){
        std::cout<<i.data()->vertex_Index1<<" "<<i.data()->vertex_Index2<<std::endl;
     }
    
}

// void test1()
// {
//     Graf* G = new Graf();    
//     G->createVertices(10);
//     G->addEdge(1, 2);
//     G->addEdge(2, 3);
//     G->addEdge(1, 5);
//     std::cout << G->vertexDegree(1)<<"\n";
//     std::cout << G->vertexDegree(8) << "\n";
//     G->printNeighbourIndices(1);
//     G->printNeighbourIndices(1);
//     std::cout << G->checkEdge(1, 2)<<"\n";
//     G->removeEdge(1, 2);
//     G->printNeighbourIndices(1);
//     std::cout << G->checkEdge(1, 2) << "\n\n\n\n\n";   
// }

// void test2()
// {
//     Graf* G = new Graf();
//     G->readFromFile("C:\\Users\\tomek\\Desktop\\algorytmy�wiczenia\\week3\\Graf1.txt");
//     G->printNeighbourIndices(1);
//     std::cout << G->getNumberOfEdges();
// }

int main()
{
    // test1();
    // test2();
    Graf* G = new Graf();
    G->addEdge(1, 2);
    G->addEdge(2, 3);
    G->addEdge(1, 5);
    std::cout<<"\nChecking edge "<<G->checkEdge(1,5)<<std::endl;
    G->print_vector(); 

    G->removeEdge(1,2);

    G->print_vector();
    std::cout<<"\nVertex Deggree: "<<G->vertexDegree(1);
    
    G->printNeighbourIndices(1);

    std::cout<<"\nTotal number of edges: "<<G->getNumberOfEdges();
}




