// Sposób postępowania:
// * Wyznaczamy najmniejszy element w ciągu a[0]... a[n-1] - zamieniamy miejscami z pierwszym elementem ciągu
// * Wyznaczamy najmniejszy element w a[1]...a[n-1] - zamieniamy z drugim elementem w ciągu...
// * Wyznaczamy najmniejszy element w a[n-2],a[n-1] - zamieniamy z (n-1)-szym elementem w ciągu.

#include <iostream>
void selection_sort(int arr[], int size){

    for(int i =0; i < size; i++){
        int min = arr[i];
        int index = i;

        //element minimalny
        for (int j=i+1; j < size; j++){
            if ( arr[j] < min){
                min = arr[j];
                index = j;
            }
            //Zamiana elementu minimalnego miejscem 
            int temp = arr[i];
            arr[i] = arr[index];
            arr[index] = temp;
        } 
    }
    std::cout<<"\nPosorotwana tablica --->> ";
    for(int k=0; k < size+1; k++){
        std::cout<<arr[k]<<" ";
    }
    std::cout<<"\n";
}


int main(){
    int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
    int N = sizeof(arr) / sizeof(arr[0]);
    selection_sort(arr, N-1);
    return 0;
}