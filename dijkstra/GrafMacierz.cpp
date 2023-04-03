#include "Graf.h"
#include <fstream>
#include <string>

int counter = 1;
Graf::Graf(){
    std::cout<<"\n\nCreating Graph"<<counter<<std::endl;
    counter = counter +1;
}
void Graf::createVertices(int amount){
    Graf::numberOfVertices = amount;
    Graf::matrix[numberOfVertices][numberOfVertices];

    for(int i=0; i < Graf::numberOfVertices; i++){
        //Debug Info
        //std::cout<<i<<" ";
        for(int j=0; j < Graf::numberOfVertices; j++){
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
void Graf::addEdge(int i, int j){
    if (Graf::checkEdge(i,j) == false){
        Graf::matrix[i][j] = 1;
    }else{    
        std::cout<<"\n Nie mozna Dodac krawedzi, wierzcholki sa juz polaczone "<<std::endl;
        return;
    }
}
void Graf::removeEdge(int i, int j){
    if(Graf::checkEdge(i,j) == true){
        Graf::matrix[i][j] = 0;
    }else{
        std::cout<<"\n Nie mozna usunac Krawedzi "<<i<<" "<<j<<" Poniewaz nie istnieje"<<std::endl;
    }
}
int Graf::vertexDegree(int idx){
    int counter=0;

    //Produkuje zły wynik jezeli podaje Graf::numberOfVertices
    // natomiast jezeli zamiast tego podam '100' wynik jest poprawny
    for(int j=0; j <  Graf::numberOfVertices; j++){
        if(Graf::matrix[idx][j] == 1){
            counter = counter+1;
            }
        }
        return counter;
    }
void Graf::print_graph(){
    std::cout<<"\nGraph "<<counter-1<<" Array Representation";
    for(int i=0; i < Graf::numberOfVertices; i++){
        for(int j=0; j < Graf::numberOfVertices; j++ ){
            if (j % Graf::numberOfVertices == 0){
                std::cout<<""<<std::endl;
            }
            std::cout<<" "<<Graf::matrix[i][j];
        }

    }
}
std::vector<int> Graf::getNeighbourIndices(int idx){
    std::vector<int> vec;

    for(int j=0; j < Graf::numberOfVertices; j++){
        if(Graf::matrix[idx][j] == 1){
            vec.push_back(j);        
        }
    }
    return vec;
}
void Graf::printNeighbourIndices(int idx){
    std::cout<<" "<<std::endl;
    std::cout<<"Siasiedzi wierzcholka: "<<idx<<std::endl;
    for(int j=0; j < Graf::numberOfVertices; j++){
        if(Graf::matrix[idx][j] == 1){
            std::cout<<j<<" ";       
        }
    }

}
int Graf::getNumberOfEdges(){
    int edges[Graf::numberOfVertices];
    for(int e=0; e < Graf::numberOfVertices; e++){
        edges[e]=0;
    }

    for(int i=0; i < Graf::numberOfVertices; i++){
        edges[i]=Graf::vertexDegree(i);
    }

    int counter = 0;
    for(int j=0; j < Graf::numberOfVertices; j++){
        if(edges[j] != 0){
            counter = counter + edges[j];
        }
    }
    return counter;
}
void Graf::readFromFile(std::string path){
    int amount_of_verticies_int;
    int edge1, edge2;
    std::string line;
    std::ifstream file_line(path);
    std::ifstream myfile(path);
    int count=0;

    //Pobranie Pierwszej liczby
    myfile >> amount_of_verticies_int;
    
    //Counting Lines in a file
    if(file_line.is_open()) 
	{
		while(file_line.peek()!=EOF)
		{
			getline(file_line, line);
			count++;
		}
		file_line.close();
        //Debug Info
		//std::cout<<"Number of lines in the file are: "<<count<<std::endl;;

    }else{
        std::cout<<"\n Cannot Open "<<path<<" file"<<std::endl;
    }

    //creating vertices
    Graf::createVertices(amount_of_verticies_int);

    for(int i=0; i < count-1; i++){
        myfile >> edge1 >>edge2;

        //Creating Edge's
        Graf::addEdge(edge1,edge2); 
    }
    //Debug Info
    //Graf::print_graph();
}
void test1()
{
    Graf* G = new Graf();    
    G->createVertices(10);
    G->addEdge(1, 2);
    G->addEdge(2, 3);
    G->addEdge(1, 5);
    G->print_graph();

    std::cout<<"\n"; 

    std::cout << G->vertexDegree(1)<<"\n";
    std::cout << G->vertexDegree(8) << "\n";
    G->printNeighbourIndices(1);
    G->printNeighbourIndices(1);
    std::cout <<"\nCheck Edge "<< G->checkEdge(1, 2)<<"\n";
    G->removeEdge(1, 2);
    G->printNeighbourIndices(1);
    std::cout <<"\nCheck Edge "<< G->checkEdge(1, 2) << "\n\n";
      
}
void test2()
{
    Graf* G = new Graf();
    G->readFromFile("GrafS.txt");
    G->printNeighbourIndices(1);
    std::cout <<"\nNumber Of edges: "<< G->getNumberOfEdges();
    G->print_graph();
}
void test3(){
    Graf* G = new Graf();
    G->readFromFile("GrafL.txt");
    G->printNeighbourIndices(1);
    std::cout <<"\nNumber Of edges: "<< G->getNumberOfEdges();

    //Nie zalecam :) Trwa 5 minut 
    //G->print_graph();

}
int main()
{
    test1();
    test2();
    test3();
    //      Mozna Odkomentowac ponizsze linie kodu, dla testu "manualnego"

    // Graf* G = new Graf();
    // G->createVertices(120);

    // G->readFromFile("GrafS.txt");

    // //Dodawanie krawedzi do wierzcholka 1
    // G->addEdge(1,2);
    // G->addEdge(1,3);
    // G->addEdge(1,4);
    // G->addEdge(1,5);

    // // Usuwanie nie istniejacej krawedzi printuje error ! tak powinno byc
    // G->removeEdge(60,60);

    // //Stopien powinien == 4, jest poprawnie
    // std::cout<<G->vertexDegree(1);

    // std::vector<int> result_vec;
    // result_vec = G->getNeighbourIndices(1);
    // //Powinno wypisac 2,3,4,5 poprawnie
    // G->printNeighbourIndices(1);

    // //Powinno wypisac 4;
    // std::cout<<"\nIlosc krawedzi ogolem \n";
    // std::cout<<G->getNumberOfEdges();

    //Print Grafu z podziałem na linie po 100 komorek (%100==0)
    //G->print_graph();

    // test1();
    // test2();  
}




