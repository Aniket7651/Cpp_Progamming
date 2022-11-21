/*
Creating first header file for some statistical formulas
functions like mean, median, standard deviation
*/

#include<cmath> // for importing power(x, n) :- x to the power of n  

// performing mean function of an int array
double Mean(int arr[], int size) {
   int i, sum = 0;       
   double avg;          
 
   for (i = 0; i < size; ++i) {
      sum += arr[i];
   }
   avg = double(sum) / size;
 
   return avg;
};

// find median of an int array
double Median(int arr[], int len){
   int term;
   // if total number of element in array will be even 
   if(len%2==0){
      term = ((len/2)+((len+1)/2))/2;
   }
   else{
      term = (len+1)/2;
   }
   return double(arr[term-1]);
}

float fact(int val){
   float fact = 1.0;
   if (val == 0 && val == 1){
      fact = 1.0;
   }
   else{
      for (int i=1; i<=val; ++i){
         fact *= i;
      }
   }
   return fact;
}

float sqrt(int n){
   return pow(float(n), 0.5);
}

float expX(float val, int n=10){
   float expo = 0.0;
   if (val == 0){
      for (int e = 1; e<=n; ++e){
         expo += 1/fact(e);
      }
   }
   else{
      for (int i = 1; i<=n; ++i){
         expo += pow(val, i)/fact(i);
      }
   }
   return 1+expo;
}

