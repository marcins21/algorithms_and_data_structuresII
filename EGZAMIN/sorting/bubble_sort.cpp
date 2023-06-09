// Sortowanie bąbelkowe
// Algorytm opiera się na zasadzie porównywania i zamiany par sąsiadujących ze sobą obiektów
// (przeglądając tablice od prawej do lewej).
// W ten sposób po pierwszym kroku algorytmu
// w lewym końcu tablicy będzie najmniejszy element; po drugim kroku pierwsze dwa elementy tablicy będą posortowane itd

#include <iostream>

void bubble_sort(int arr[], int size){
    for(int i=0; i < size; i++){
        for(int j=0; j < size-i; j++)
        {
            if (arr[j] > arr[j+1]){
                //Zamienienianie kolejnoscia niepoprawnych elemntów
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }

    std::cout<<"\nPosortowana Tablica -->> ";
    for(int k=0; k < size+1; k++){
        std::cout<<arr[k]<<" ";
    }
    std::cout<<"\n";

}

int main(){
    int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
    int N = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, N-1);
    return 0;
}