/*
This C++ program file created for the running task from python interpreter
compiled as for_Cpp_py.exe
*/
#include"userlibC++/statistics.h"
#include"userlibC++/struc++.h"
#include<iostream>
using namespace std;

// driver function.....
int main(){
    int arr[] = {28, 84, 19, 10, 72};
    cout << "mean of an array: " << Mean(arr, 5) << endl;

    // finding length of an array
    int sizeofarr = sizeof(arr);
    int length = sizeofarr/sizeof(int);
    cout << "Index of a value in an array: " << Index(arr, 84, length) <<endl;
    cout << "median: " << Median(arr, length) <<endl;
    cout << "exponential: " << expX(0);
    return 0;
}
