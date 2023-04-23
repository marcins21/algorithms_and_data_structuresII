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
                #print(f"\nElement '{element}' successfully added at '{element}' index")
                return True
            print(f"\nElement already exists in set")
            return False
        return False

    def withdraw(self,element):
        if self.check_validity_of_element(element):
            if self.arr[element] == 1:
                self.arr[element] = 0
                #print(f"\nElement '{element}' successfully deleted from index '{element}'")
                return True
            print(f"\nElement doesn't exists in set")
            return False
        return False

    def is_in_set(self,element):
        if element in self.arr:
            return True
        return False
    
    def __add__(self,other: 'MatrixSet'):
        size_of_smaller = min(other.size,self.size)
        new_arr = [0 for i in range(size_of_smaller)]
        for i in range(size_of_smaller):
            if other.arr[i] == 1 or self.arr[i] == 1:
                new_arr[i] = 1
        return new_arr
    
    def __sub__(self,other: 'MatrixSet'):
        new_arr = [0 for k in range(self.size)]
        for i in range(other.size):
            if other.arr[i] != self.arr[i]:
                new_arr[i] = 1
        return new_arr
    
    def __mul__(self,other: 'MatrixSet'):
        new_arr = [0 for i in range(self.size)]
        for i in range(self.size):
            if self.arr[i] == other.arr[i]:
                new_arr[i] = 1
        return new_arr

def main():
    ms1 = MatrixSet(10)
    ms1.insert(1)
    ms1.insert(2)
    ms1.insert(3)
    ms1.insert(6)

    print("\nms1 Set")
    ms1.print_matrix()


    ms2 = MatrixSet(10)
    ms2.insert(6)
    ms2.insert(7)
    ms2.insert(8)
    print("\nms2 Set")
    ms2.print_matrix()
    
    print()
    print(f"Operacja dodawania '+' --> {ms1+ms2}")
    print(f"Operacja odejmowania '-' --> {ms1-ms2}")
    print(f"Operacja Czesc wspolna '*' --> {ms1*ms2}")

main()
