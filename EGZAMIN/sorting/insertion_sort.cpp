// Dla każdego i=2, 3,...,n należy powtarzać wstawianie a[i] w już uporządkowaną część listy a[1]≤... ≤a[i-1]

#include <iostream>
void insertion_sort(int arr[], int size){

    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
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
    insertion_sort(arr, N-1);
    return 0;
}