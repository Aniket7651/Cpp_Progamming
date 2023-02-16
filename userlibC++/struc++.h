/*
struc++.h is a header file that will be use as a pre-define structures
like, adding a value in arrays and finding a value in array, adding a
element at the specific position in array
*/

// array function for finding index of an element in an array, return 0 if element will not 
// exists in perticular array
int Index(int arr[], int value, int size){
    int index;
    for (int i=0; i<size; i++){
        if (arr[i] == value){
            index = i;
        }
    }
    return index;
}
