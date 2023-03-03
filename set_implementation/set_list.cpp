#include "setList.h"
#include <algorithm>

int setList::getSize(){
    return vec.size();
}

void setList::printSet(){
    int vec_size = setList::getSize();
    for(int i=0; i < vec_size; i++ ){
        std::cout<<vec.at(i)<<" ";
    }
}

void setList::insertion(int x){
    if(isInSet(x)){
        std::cout<<"\nElement "<<x<<" Already in a set"<<std::endl;
    }else{
        vec.push_back(x);
    }
}

bool setList::isInSet(int x) {
    int element = x;
    auto it = std::find(vec.begin(), vec.end(), element);
    if (it != vec.end()) {
        return true;
    } else {
        return false;
    }
}

void setList::withdraw(int x){
    if(!isInSet(x)){
        std::cout<<"\nElement "<<x<<" Already has beeen deleted"<<std::endl;
    }else{
        std::vector<int>::iterator it = std::find(vec.begin(), vec.end(), x);
        int index = std::distance(vec.begin(), it);
        vec.erase(vec.begin()+index);
    }
}

setList setList::operator+(setList& obj){
    setList res = *this; 
    for (int x : obj.vec) {
        if (!res.isInSet(x)) { 
            res.vec.push_back(x);
            }
        }
    return res;
    }

   
setList setList::operator-(setList& obj){
    setList res = *this; 
    for (int x : obj.vec) {
        res.withdraw(x); 
    }
    return res;
}

setList setList::operator*(setList& obj){
    setList res;
    for (int x : obj.vec) {
        if (isInSet(x)) { // dodajemy tylko elementy, które są w obu setach
            res.vec.push_back(x);
        }
    }
    return res;
}

bool setList::operator==(setList& obj){
    if (vec.size() != obj.vec.size()) { 
        return false;
    }
    for (int x : obj.vec) {
        if (!isInSet(x)) { 
            return false;
        }
    }
    return true;
}

bool setList::operator<=(setList& obj){
    for (int x : vec) {
        if (!obj.isInSet(x)) { 
            return false;
        }
    }
    return true;
}


int main(){
    setList list1;
    setList list2;
    setList lista3;

    list1.insertion(10);
    list1.insertion(12);
    list1.insertion(13);

    list2.insertion(20);
    list2.insertion(22);
    list2.insertion(23);

    std::cout<<"\n Lista1 :"<<std::endl;
    list1.printSet();

    std::cout<<"\n Lista2 : "<<std::endl;
    list2.printSet();

    lista3 = list1 + list2;
    std::cout<<" \nLista3 = Lista1 + Lista2 "<<std::endl;
    lista3.printSet(); 

    setList lista4 = list1 * list2;
    std::cout<<" \nLista4 = Lista1 * Lista2 "<<std::endl;
    lista4.printSet(); 

    setList lista5 = list1 - list2;
    std::cout<<" \nLista5 = Lista1 - Lista2 "<<std::endl;
    lista5.printSet();

    bool areEqual = (list1 == list2);
    std::cout<<" \nList1 == List2: "<<areEqual<<std::endl; 

    bool isSubset = (list1 <= lista3);
    std::cout<<" \nList1 <= Lista: "<<isSubset<<std::endl;;
    return 0;
}