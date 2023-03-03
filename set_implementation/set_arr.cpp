#include "setArr.h"




setArr::setArr(){
    size=100;
    table=new bool[size];
    
    /* 
        Ustawienie wszystkich komorek na False
        Niestety u mnie kompilator domsylnie nie ustawia wszystkich boolean'ow na false
    */
    for(int i=0; i < size; i++){
        table[i]=false; 
    }
}

int setArr::getSize(){
    return size;
}

void setArr::clearSet(){

    /* Ustawienie wszystkich komorek na False*/
    for(int i=0; i < size; i++){
        table[i]=false; 
    }

}

void setArr::printSet(){
    int array_size = setArr::getSize();
    for(int i=0; i < size; i++){
        if (table[i] == true){
            std::cout<<i<<" ";
        }
    }
}

void setArr::insert(int x){
    bool is_x_exists = setArr::isInSet(x);
    bool correctNumber = setArr::checkRangeCorrectness(x);
    if (correctNumber==true){
        if (is_x_exists == false){
            table[x]=true;
        }else{
            std::cout<<"\nLiczba "<<x<<" Juz istnieje w zbiorze"<<std::endl;
        }
    }
    else{
        std::cout<<"\nPodana liczba jest spoza przedzialu 0-100"<<x<<std::endl;
    }  
}

void setArr::withdraw(int i){
    bool correctNumber = setArr::checkRangeCorrectness(i);
    bool is_i_exists = setArr::isInSet(i);
    if (correctNumber == false){
        std::cout<<"\nPodano zly numer przyjmuje numery od -99 do +99"<<std::endl;
    }
    if (is_i_exists == true){
        table[i]=false;
    }
    else{
        std::cout<<"\nPodana liczba nie istnieje "<<std::endl;
    }

}
bool setArr::isInSet(int i){
    if (table[i] == true){
        return true;
    }
    else{
        return false;
    }
}
bool setArr::checkRangeCorrectness(int x){
    if ((x < setArr::universeSize) && (x > 0)){
        return true;
    }
    else{
        return false;
    }
}


// Operator dodawania zbiorów
setArr setArr::operator+(setArr& object){
    setArr result; 

    for(int i=0; i<universeSize; i++){ 
        if(table[i] || object.isInSet(i)){ 
            result.insert(i); 
        }
    }

    return result; 
}

// Operator iloczynu zbiorów
setArr setArr::operator*(setArr& object){
    setArr result; 

    for(int i=0; i<universeSize; i++){ 
        if(table[i] && object.isInSet(i)){ 
            result.insert(i); 
        }
    }

    return result; 
}



// Operator różnicy zbiorów
setArr setArr::operator-(setArr& object){
    setArr result;

    for(int i=0; i<universeSize; i++){ 
        if(table[i] && !object.isInSet(i)){ 
            result.insert(i); 
        }
    }

    return result; 
}

// Operator rownosci zbiorow
bool setArr::operator==(setArr& object){
    for(int i=0; i<universeSize; i++){
        if(table[i] != object.isInSet(i)){ 
            return false; 
        }
    }

    return true; 
}

//Operator podzbioru
bool setArr::operator<=(setArr& object){
    for(int i=0; i<universeSize; i++){ 
        if(table[i] && !object.isInSet(i)){ 
            return false; 
        }
    }

    return true; 
}



int main(){
  /* SetArray Object*/
    setArr set_array;
    setArr set_array1;

    set_array.insert(9);
    set_array.insert(7);
    set_array.insert(10);
    set_array.insert(20);
    set_array.insert(21);
    set_array.insert(19);

    set_array.withdraw(19);
    std::cout << "Array1:" << std::endl;
    set_array.printSet();   

    set_array1.insert(9);
    set_array1.insert(10);

    std::cout << "\nArray2:" << std::endl;
    set_array1.printSet();

    setArr set_array3 = set_array + set_array1; // dodajemy zbiory
    setArr set_array4 = set_array - set_array1; // różnica zbiorów

    std::cout << "\nRoznica:" << std::endl;
    set_array4.printSet();

    if(set_array == set_array1) {
        std::cout << "\nZbiory sa rowne." << std::endl;
    } 
    else {
        std::cout << "\nZbiory sa rozne." << std::endl;
    }

    if(set_array <= set_array3) {
        std::cout << "\nArray1 jest podzbiorem Array3 --> Array1+Array2." << std::endl;
    } 
    else {
        std::cout << "\nArray1 nie jest podzbiorem Array3 --> Array1+Array2." << std::endl;
    }

return 0;

}


