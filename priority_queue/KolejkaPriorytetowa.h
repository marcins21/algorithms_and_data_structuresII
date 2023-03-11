#pragma once
#include <array>

using namespace std;


class KolejkaPriorytetowa
{
    public:
    void insert(int x);
    int RemoveRootElem();
    void print();   //opcjonalnie dla wyswietlenia kolejnych elementow macierzy, w ktorej trzymany jest kopiec.
    int getRootElem();
    
};