//projectEuler4.cpp
#include <iostream>
#include <time.h>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;


int myPow(int x, int p)
{
  if (p == 0) return 1;
  if (p == 1) return x;

  int tmp = myPow(x, p/2);
  if (p%2 == 0) return tmp * tmp;
  else return x * tmp * tmp;
}
int nthdigit(int n, int num){
    if(n==1){
        return num%myPow(10,n);
    }
    else{
        return (num%myPow(10,n)-num%myPow(10,n-1))/myPow(10,n-1);
    } 
}

bool is_palindrome(int num){
    int digits = 0;
    while (num%myPow(10,digits)!=num){
        digits++;
    }
    for (int n=1;n<=digits/2;n++){
        if (nthdigit(n,num)!=nthdigit(digits-n+1,num)){ 
            return false;
        }
    }
    return true;
}

int largest_palindrome_nums(int digits){
    int max = 0;
    int candidate;
    int start = myPow(10,digits-1);
    int end = myPow(10,digits);
    for (int i=start;i<end;i++){
        for (int j=i;j<end;j++){
            candidate = i*j;
            if (is_palindrome(candidate) && candidate>max){
                max = candidate;
            }
        }
    }
    return max;
}


int main(){
    clock_t t1, t2;
    t1=clock();
    int digits = 3;
    int max = largest_palindrome_nums(digits);
    t2=clock();
    cout<<"Max palindrome product of "<<digits<<" digit numbers is "<<max<<endl;
    double diff = ((double)t2-(double)t1)/CLOCKS_PER_SEC;
    cout<<"Time elapsed: "<<diff<<endl;
    return 0;
}