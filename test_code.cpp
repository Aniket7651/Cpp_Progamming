/*
This C++ program file created for the running task from python interpreter
compiled as for_Cpp_py.exe
*/
#include"userlibC++/statistics.h"
#include<iostream>
using namespace std;

// driver function.....
int main(){
    int arr[10] = {28, 84, 19, 10, 72};
    int size = sizeof(arr);
    cout << "Avg. of an array: " << getAverage(arr, 5) << endl;
    cout << "size of your array: " << size;
    return 0;
}
