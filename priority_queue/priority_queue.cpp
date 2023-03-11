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

// Shifting node, and maintaing heap structure
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
    //TODO
    return 0;
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
    q1.print();

    int root = q1.getRootElem();
    std::cout<<"root element"<<root<<std::endl;
    
    std::cout<<"\nHello World!\n";
    return 0;
}