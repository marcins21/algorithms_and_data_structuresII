#pragma once
#include <array>

using namespace std;


class KolejkaPriorytetowa
{
    public:
    void insert(int x);
    int RemoveRootElem();
    void print();   //opcjonalnie dla wyœwietlenia kolejnych elementów macierzy, w której trzymany jest kopiec.
    int getRootElem();
    
};