#include <iostream>
#include <cmath>
#include <time.h>
#include <vector>
using namespace std;
int main(){
    clock_t t1, t2;
    t1=clock();
    vector<unsigned int> counts(1000000);
    unsigned int max = 0;
    unsigned int maxint, count, j;
    for (unsigned int i=1;i<=1000000;i++){
        count = 1;
        j = i;
        while(j!=1){
            if (j<i){ count += counts.at(j-1)-1; break; }
            if (j%2==0){ j /= 2;}
            else{ j = 3*j+1; }
            count++;
        }
        counts.at(i-1) = count;
        if (count>max){
            maxint = i; max = count;
        }
        //cout<<"i = "<<i<<endl;
    }
    cout<<"max ="<<max<<endl;
    cout<<"maxint ="<<maxint<<endl;
    t2=clock();
    double diff = ((double)t2-(double)t1)/CLOCKS_PER_SEC;
    cout<<"Time elapsed: "<<diff<<endl;
    return 0;
}