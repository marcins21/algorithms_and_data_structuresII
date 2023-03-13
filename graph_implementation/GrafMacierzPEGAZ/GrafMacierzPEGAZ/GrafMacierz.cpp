#include "Graf.h"



// Done
Graf::Graf(){
    Graf::matrix[100][100];
    Graf::numberOfVertices;

    for(int i=0; i < 100; i++){
        for(int j=0; j < 100; j++){
            Graf::matrix[i][j] =0;
        }
    }
}

bool Graf::checkEdge(int i, int j){
    if(Graf::matrix[i][j]==1){
        return true;
    }else{
        return false;
    }
}

// Done 
void Graf::addEdge(int i, int j){
    if (Graf::checkEdge(i,j) == false){
        Graf::matrix[i][j] = 1;
    }else{    
        std::cout<<"\n Nie mozna Dodac krawedzi, wierzcholki sa juz polaczone "<<std::endl;
        return;
    }
}

// Done
void Graf::removeEdge(int i, int j){
    if(Graf::checkEdge(i,j) == true){
        Graf::matrix[i][j] = 0;
    }else{
        std::cout<<"\n Nie mozna usunac Krawedzi "<<i<<" "<<j<<" Poniewaz nie istnieje"<<std::endl;
    }
}


// Done
int Graf::vertexDegree(int idx){
    int counter=0;
    for(int j=0; j < 100; j++){
        if(Graf::matrix[idx][j] == 1){
            counter = counter+1;
            }
        }
        return counter;
    }


// Done
void Graf::print_graph(){
    for(int i=0; i < 100; i++){
        for(int j=0; j < 100; j++ ){
            if (j % 100 == 0){
                std::cout<<""<<std::endl;
            }
            std::cout<<" "<<Graf::matrix[i][j];
        }

    }
}

// Done
std::vector<int> Graf::getNeighbourIndices(int idx){
    std::vector<int> vec;

    for(int j=0; j < 100; j++){
        if(Graf::matrix[idx][j] == 1){
            vec.push_back(j);        
        }
    }
    return vec;
}

// Done
void Graf::printNeighbourIndices(int idx){
    std::cout<<" "<<std::endl;
    std::cout<<"Siasiedzi wierzcholka: "<<idx<<std::endl;
    for(int j=0; j < 100; j++){
        if(Graf::matrix[idx][j] == 1){
            std::cout<<j<<" ";       
        }
    }

}


// Done
int Graf::getNumberOfEdges(){
    int edges[100];
    for(int e=0; e < 100; e++){
        edges[e]=0;
    }

    for(int i=0; i < 100; i++){
        edges[i]=Graf::vertexDegree(i);
    }

    int counter = 0;
    for(int j=0; j < 100; j++){
        if(edges[j] != 0){
            counter = counter + edges[j];
        }
    }
    return counter;
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
//     G->readFromFile("C:/Users/msitk/Desktop/Programowanie/aisd2-cw/graph_implementation/GrafS.txt");
//     G->printNeighbourIndices(1);
//     std::cout << G->getNumberOfEdges();
// }

int main()
{
    Graf* G = new Graf();

    //Dodawanie krawedzi do wierzcholka 1
    G->addEdge(1,2);
    G->addEdge(1,3);
    G->addEdge(1,4);
    G->addEdge(1,5);

    // Usuwanie nie istniejacej krawedzi printuje error ! tak powinno byc
    G->removeEdge(60,60);

    //Stopien powinien == 3, jest poprawnie
    std::cout<<G->vertexDegree(1);


    std::vector<int> result_vec;
    result_vec = G->getNeighbourIndices(1);
    //Powinno wypisac 2,3,4 poprawnie
    G->printNeighbourIndices(1);

    //Powinno wypisac 3;
    std::cout<<"\nIlosc krawedzi ogolem\n";
    std::cout<<G->getNumberOfEdges();
    


    //Print Grafu z podziałem na linie po 100 komorek (%100==0)
    //G->print_graph();

    // test1();
    // test2();  
}




