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
        return obj;
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
    list1.insert(10);
    list1.insert(12);
    list1.insert(13);

    list1.withdraw(13);

    list1.printSet();

    std::cout<<"\nHello World!";
    return 0;
}