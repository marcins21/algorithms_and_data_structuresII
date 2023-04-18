# Implementacja zbioru 
import numpy as np


#array implementation
class MatrixSet:
    def __init__(self,size):
        self.size = size
        self.arr = [0 for i in range(size)]

    def print_matrix(self):
        print(self.arr)

    def check_validity_of_element(self,element):
        if element > len(self.arr) or element < 0:
            print(f"\nElement '{element}' is to hight for array of size '{self.size}'")
            return False
        return True

    def insert(self,element):
        if self.check_validity_of_element(element):
            if self.arr[element] == 0:
                self.arr[element] = 1
                print(f"\nElement '{element}' successfully added at '{element}' index")
                return True
            print(f"\nElement already exists in set")
            return False
        return False

    def withdraw(self,element):
        if self.check_validity_of_element(element):
            if self.arr[element] == 1:
                self.arr[element] = 0
                print(f"\nElement '{element}' successfully deleted from index '{element}'")
                return True
            print(f"\nElement doesn't exists in set")
            return False
        return False

        



# • Insert - dodaje element do zbioru
# • Withdraw – usuwa element ze zbioru
# • isInSet - sprawdza czy dany element jest we zbiorze
# • suma – zwraca sumę dwóch zbiorów (elementy nie duplikują się, jeśli są w obu sumowanych
# zbiorach)
# • część wspólna – zwraca część wspólną dwóch zbiorów (elementy które są jednocześnie w
# jednym i w drugim zbiorze)
# • różnica (A-B) -usuwa ze zbioru A elementy, które są także w B.
# • równość – sprawdza czy oba zbiory zawierają dokładnie te same elementy
# • zawieranie - sprawdza, czy zbiór B jest podzbiorem zbioru A (tzn. czy wszystkie elementy B są
# elementami A)

def main():
    ms = MatrixSet(10)
    ms.print_matrix()
    ms.insert(9)
    ms.insert(9)
    ms.print_matrix()
    ms.withdraw(9)
    ms.withdraw(9)
    ms.print_matrix()


main()