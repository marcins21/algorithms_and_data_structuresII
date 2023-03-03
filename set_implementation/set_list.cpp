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

void setList::insert(int x){
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

/*TOOD Operators*/
    setList setList::operator+(setList& obj){
        setList res;
        res.vec.insert(vec.begin(),obj.vec.begin(),obj.vec.end())
        return res;
       
    }

    setList setList::operator*(setList& obj){
        return obj;
    }
      
    setList setList::operator-(setList& obj){
        return obj;
    }
    
    bool setList::operator==(setList& obj){
        return true;
    }
    bool setList::operator<=(setList& obj){
        return true;
    }

int main(){

    setList list1;
    setList list2;
    setList lista3;

    list1.insert(10);
    list1.insert(12);
    list1.insert(13);

    list2.insert(20);
    list2.insert(22);
    list2.insert(23);

    std::cout<<" Lista1 "<<std::endl;
    list1.printSet();
    std::cout<<" \nLista2 "<<std::endl;
    list2.printSet();

    lista3 = list1 + list2;
    std::cout<<" \nLista3 "<<std::endl;
    lista3.printSet();

    std::cout<<"\nHello World!";
    return 0;
}