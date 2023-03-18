#include <iostream>
#include "KolejkaPriorytetowa.h"

// Priority Queue With HEAP
// Zadeklarowanie Wielkosci Drzewa
int H[40];
int size = -1;

int parent(int i){
    return (i-1) / 2;
}
int leftChild(int i){
    return ((2*i) + 1);
}
int rightChild(int i){
    return ((2*i)+2);
}

void maintain_heap_structure(int i){
    while (i > 0 && H[parent(i)] < H[i]){
        swap(H[parent(i)],H[i]);
        i=parent(i);
    }
}
void KolejkaPriorytetowa::insert(int x){
    size = size+1;
    H[size] = x;
    maintain_heap_structure(size);
}
int KolejkaPriorytetowa::getRootElem(){
    return H[0];
}
int KolejkaPriorytetowa::RemoveRootElem(){
    if(size < 0){ 
        return -1; 
    }
    int root = H[0];
    H[0] = H[size];
    size = size-1;

    int i = 0;
    while (i <= size){
        int max = i;
        if (leftChild(i) <= size && H[leftChild(i)] > H[max]){
            max = leftChild(i);
        }
        if (rightChild(i) <= size && H[rightChild(i)] > H[max]){
            max = rightChild(i);
        }
        if (max != i){
            swap(H[i], H[max]);
            i = max;
        }
        else{ 
            break;
        }
    }

    return root;
}
void KolejkaPriorytetowa::print(){
    for (int i=0; i <= size ; i++){
        std::cout<<H[i]<<std::endl;
        if( i % 2 == 0){
            std::cout<<std::endl;
        }
    }
}
int main(){

    KolejkaPriorytetowa q1;

    q1.insert(45);
    q1.insert(10);
    q1.insert(14);
    q1.insert(12);

    std::cout << "Kolejka po wstawieniu elementow: " << std::endl;
    q1.print();

    int root = q1.getRootElem();
    std::cout<<"Wartosc korzenia: "<<root<<std::endl;

    int removed = q1.RemoveRootElem();
    std::cout<<"Usuniety element: "<<removed<<std::endl;

    std::cout << "Kolejka po usunieciu korzenia: " << std::endl;
    q1.print();

    root = q1.getRootElem();
    std::cout<<"Nowa wartosc korzenia: "<<root<<std::endl;


    std::cout<<std::endl;
    q1.print();
    return 0;
}




