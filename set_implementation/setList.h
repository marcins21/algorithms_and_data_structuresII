#pragma once
#include<iostream>
#include <vector>

class setList
{
    std::vector<int> vec;

public:

    int getSize();  
    void printSet(); 
    void insertion(int x);
    void withdraw(int x);
    bool isInSet(int x); 
    setList operator+(setList& obj);  
    setList operator*(setList& obj);   
    setList operator-(setList& obj);
    bool operator==(setList& obj);  
    bool operator<=(setList& obj);
    
};


